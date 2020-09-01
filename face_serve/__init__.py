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
姓名列表如果已修改需要重新获取
'''
name_list_dirty = 0


'''
Redis 客户端连接
'''
redisConn = redis.StrictRedis(host='redis', port=6379, decode_responses=True)
pipeline = redisConn.pipeline(transaction=True)


def reload_all_users():
    return redisConn.keys('face:*')


'''
所有用户key保存于内存中留待复用
'''
all_users = reload_all_users()
