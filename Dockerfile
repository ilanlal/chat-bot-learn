FROM python:3.10-slim

WORKDIR /app

COPY . ./

RUN pip install flask gunicorn googlesearch-python gspread cydifflib

CMD gunicorn --bind :$PORT app:app