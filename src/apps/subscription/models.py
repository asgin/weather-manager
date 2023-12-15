from django.db import models
from apps.user.models import WeatherManagerUser
from apps.weather.models import City

class Subscription(models.Model):
    choices = [
        (2, '2 hours'),
        (6, '6 hours'),
        (12, '12 hours'),
    ]
    user = models.ForeignKey(WeatherManagerUser, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    send_every_hours = models.IntegerField(choices=choices)