from django.db import models
from apps.user.models import WeatherManagerUser
from apps.city.models import City

class Subscription(models.Model):
    user = models.ForeignKey(WeatherManagerUser, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    send_every_hours = models.IntegerField()
    