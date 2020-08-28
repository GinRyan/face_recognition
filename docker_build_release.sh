export BUILD_TAG=face_recog:0.0.1-release
docker build .  -t $BUILD_TAG -f Dockerfile.release
docker run -p 10000:10000 $BUILD_TAG
