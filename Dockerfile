FROM python:3.10-slim
LABEL "creator"="RoryMercury"

WORKDIR /code
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY project project/
COPY tests tests/
COPY src src/
COPY wsgi.py .

RUN pytest -s -v tests/*
CMD flask run -h 0.0.0.0 -p 5000