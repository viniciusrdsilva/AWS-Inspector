FROM python:3.8-slim

WORKDIR /app

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./src /app/

RUN python /app/Root-Monitoring.py