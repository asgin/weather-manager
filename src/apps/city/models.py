from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)
    weather_info = models.JSONField(null=True)