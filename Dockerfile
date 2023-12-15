FROM python:3.11-alpine3.16

COPY . .
RUN apk add postgresql-dev build-base postgresql-client
RUN pip install -r requirements.txt
WORKDIR /src
RUN python manage.py makemigrations



EXPOSE 8000