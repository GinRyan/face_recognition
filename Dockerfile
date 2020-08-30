# For more information, please refer to https://aka.ms/vscode-docker-python
FROM registry.cn-hangzhou.aliyuncs.com/sakamoto/face-recog:0.1-cloudbuild

EXPOSE 10000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1


ADD . /app
WORKDIR /app

# Install pip requirements
RUN python -m pip install -r requirements.txt

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "face_serve.face_recog_service:app"]
