# pull official base image
#!/bin/sh
FROM python:3.8.5
# set work directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY ./requirements.txt .

RUN pip3 install --upgrade pip setuptools -r requirements.txt


COPY . .

EXPOSE 8000

# CMD ['cd', './lottee']
# CMD ['python', 'manage.py', 'migrate']
# CMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']
