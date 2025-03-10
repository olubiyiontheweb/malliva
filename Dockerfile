FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /app
ENV MALLIVA_ENVIRONMENT='DEVELOPMENT'
COPY . /app
RUN pip install -r requirements.txt