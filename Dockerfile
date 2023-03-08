FROM python:3.10-alpine

# Installa i pacchetti necessari per psycopg2
RUN apk add --no-cache postgresql-dev gcc musl-dev

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG DEBUG
ARG SECRET_KEY
ARG DISCORD_SERVICE_API_KEY
ARG TELEGRAM_SERVICE_API_KEY

COPY ./src .
COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

# self starting app after build
# if the app its build directly from this dockerfile then the 80 port will not be automatically linked
CMD python manage.py migrate --noinput
CMD gunicorn Pavlov.wsgi:application --bind 0.0.0.0:8000
