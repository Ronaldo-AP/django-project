FROM python:3.10-slim

RUN apt update -y && apt upgrade -y
RUN pip install --upgrade pip
RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

# Project initialization:
RUN pipenv install --system --deploy --ignore-pipfile

# Copy project files
COPY EchoWolfProject /app/EchoWolfProject/

EXPOSE 80