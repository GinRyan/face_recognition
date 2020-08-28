FROM facerecog-base:0.1

EXPOSE 10000

COPY .  /app

WORKDIR /app

ENV FLASK_APP=face_recog_service.py \
    FLASK_ENV=production \
    FLASK_DEBUG=0 

ENTRYPOINT [ "python3" , "-m" , "flask" , "run" , "--host=0.0.0.0" , "--port=10000"] 