FROM python:3.7

COPY . /app
WORKDIR /app/

ENV PYTHONPATH=/app

RUN pip install gunicorn && pip install -r /app/requirements.txt

ENV PORT 8082
ENV TIMEOUT 60
ENV WORKERS 1


CMD gunicorn --bind 0.0.0.0:$PORT --workers $WORKERS --timeout $TIMEOUT monitoring-mock:app

