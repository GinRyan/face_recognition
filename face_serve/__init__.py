from minio import Minio
from minio.error import ResponseError
import redis

'''
Minio 连接
'''
minioClient = Minio('minio1:9000',
                  access_key='minioStorage',
                  secret_key='minioStorage123',
                  secure=False)
'''
bucket name 
存储桶名称
'''
user_face_image_bucket = 'userfaceimage'

'''
Redis 客户端连接
'''
redisConn = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)   
pipeline = redisConn.pipeline(transaction=True)

