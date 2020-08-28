export BUILD_TAG=registry.cn-hangzhou.aliyuncs.com/sakamoto/face-recog-serve:0.0.1-prod
docker build .  -t $BUILD_TAG -f Dockerfile
#docker run -p 10000:10000 $BUILD_TAG
