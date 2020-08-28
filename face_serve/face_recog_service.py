from datetime import datetime
import face_recognition as face
import re
from flask import Flask, jsonify, request, redirect
import pickle as pkl
import os
from werkzeug.utils import secure_filename

# 分布式存储minio客户端读取器
from . import minioClient
from . import user_face_image_bucket
# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
USE_MINIO = os.environ['USE_MINIO']

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return "Hello, Face!"


@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content


@app.route("/upload/<name>")
def upload_image_file(name):
    if request.method == 'POST':
        if 'file' not in request.files:
            return "Lack of 'file' ;_; "

        file = request.files['file']
        filename = file.filename

        if filename == '':
            filename = name + '.unknown'
            return 'File ' + filename + ' not a allowed file.'
        if file and allowed_file(filename):
            filename = str(datetime.now()) + "_" + secure_filename(filename)
            tmpfile = '/var/www/upload/' + filename
            print('Save temp file: ' + tmpfile)
            file.save(tmpfile)
            ret = defect_face_and_save_file(name, tmpfile, file.mimetype)
            return ret


def defect_face_and_save_file(name, face_image_file, mimetype):
    '''
    根据给定的图片文件检测脸并且存在命名为name的目录中。

    :param name: 上传图片用户的名称
    :param face_image_file: 图片文件路径
    :param mimetype: 图片文件mimetype
    :return: 返回可能的脸的用户名称
    '''
    ret = {'msg': '', 'code': 0}
    imagedata = face.load_image_file(face_image_file)
    faces_count = len(face.face_locations(imagedata))
    if faces_count == 0:
        ret['msg'] = 'No face detected!'
        ret['code'] = -1
        return jsonify(ret)

    elif faces_count > 1:
        ret['msg'] = 'Multi faces detected!'
        ret['code'] = -2
        return jsonify(ret)

    elif faces_count == 1:
        ret['msg'] = 'Success!'
        ret['code'] = 0
        ret['infer'] = 'Unknown face.'
        # 1、存储这张脸的图片(opt: 可切换开关)
        if USE_MINIO == 1 or USE_MINIO == True:
            bucket_exist = minioClient.bucket_exists(user_face_image_bucket)
            if bucket_exist:
                minioClient.fput_object(bucket_name=user_face_image_bucket, object_name=name, file_path=face_image_file, content_type=mimetype)
        
        # 2、存储这张脸的图片的128维脸部描述符编码

        return jsonify(ret)
