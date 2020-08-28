from minio import Minio
from minio.error import ResponseError

minioClient = Minio('minio_host',
                  access_key='minioStorage',
                  secret_key='minioStorage123',
                  secure=True)
'''
bucket name 
存储桶名称
'''
user_face_image_bucket = 'userfaceimage'
