FROM python:3.10-slim

WORKDIR /app

COPY . ./

RUN pip install flask gunicorn difflib googlesearch gspread

CMD gunicorn --bind :$PORT app:app