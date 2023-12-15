from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)

class Weather(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    main_weather = models.CharField(max_length=255)
    temp = models.FloatField()
    feels_like = models.FloatField()
    speed_wind = models.FloatField()