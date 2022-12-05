FROM python:3.10-slim

LABEL "creator"="RoryMercury"

RUN apt update -y
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY project project/
COPY tests tests/
COPY src src/

RUN pytest -s -v tests/*
CMD flask run -h 0.0.0.0 -p 80