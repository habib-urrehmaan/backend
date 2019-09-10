FROM python:3.6-alpine

RUN pip install flask

ADD app.py /

EXPOSE 8080

CMD [ "python", "./app.py" ]