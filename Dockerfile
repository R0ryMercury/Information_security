FROM python:3.10-slim

RUN apt update -y
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY project project/
COPY docker_config-ci.py project/config.py
CMD flask run -h 0.0.0.0 -p 80