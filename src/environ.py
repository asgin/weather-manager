import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')
DB_PORT = os.environ.get('DB_PORT')
DB_ENGINE = os.environ.get('DB_ENGINE') 
WEATHER_LINK = os.environ.get('WEATHER_LINK')
REDIS_URL = os.environ.get('REDIS_URL')
SECRET_KEY = os.environ.get('SECRET_KEY')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USERNAME = os.environ.get('EMAIL_HOST_USERNAME')