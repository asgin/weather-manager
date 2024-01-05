from config.celery_app import app
import requests
from apps.city.models import City
from config.environ import WEATHER_LINK

@app.task()
def update_weather_info():
    updated_weather_info_cities = []
    for model in City.objects.all():
        weather_info = requests.get(WEATHER_LINK.format(model.name)).json()
        model.weather_info = weather_info
        model.save()
        updated_weather_info_cities.append(model.name)
    return f'Updated successfully for {updated_weather_info_cities}'