FROM facerecog-base:0.1

CMD cd /root/face_recognition/examples && \
    python3 recognize_faces_in_pictures.py
