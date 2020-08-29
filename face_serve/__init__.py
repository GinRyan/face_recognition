from minio import Minio
from minio.error import ResponseError

minioClient = Minio('minio1:9000',
                  access_key='minioStorage',
                  secret_key='minioStorage123',
                  secure=False)
'''
bucket name 
存储桶名称
'''
user_face_image_bucket = 'userfaceimage'
