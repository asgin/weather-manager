import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('app')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "update_weather_info_every_hour": {
        "task": "apps.weather.tasks.update_weather_info",
        "schedule": crontab(hour="*/1"),
    },
    "send_weather_info_every_two_hours": {
        "task": "apps.subscription.tasks.send_weather_info_every_2_hours",
        "schedule": crontab(hour="*/2"),
    },
    "send_weather_info_every_six_hours": {
        "task": "apps.subscription.tasks.send_weather_info_every_6_hours",
        "schedule": crontab(hour="*/6"),
    },  
    "send_weather_info_every_twelve_hours": {
        "task": "apps.subscription.tasks.send_weather_info_every_12_hours",
        "schedule": crontab(hour="*/12"),
    }
}