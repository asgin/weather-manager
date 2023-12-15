from config.celery_app import app
import requests
from apps.weather.models import City
from apps.weather.services import update_weather
from environ import WEATHER_LINK

@app.task()
def update_weather_info():
    for model in City.objects.all():
        weather_info = requests.get(WEATHER_LINK.format(model.name)).json()
        update_weather(weather_info, model)
        return 'Updated successfully for {}'.format(model.name)
