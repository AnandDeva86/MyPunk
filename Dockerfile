FROM python:3.6

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt

RUN pip install -e .
