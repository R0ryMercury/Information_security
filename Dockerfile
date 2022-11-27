FROM python:3.10-slim

RUN apt update && apt install ffmpeg libsm6 libxext6  -y
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY project project/
COPY docker_config.py project/config.py

CMD flask run -h 0.0.0.0 -p 80