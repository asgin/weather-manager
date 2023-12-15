from django.db import models
from django.contrib.auth.models import AbstractUser

class WeatherManagerUser(AbstractUser):
    email = models.EmailField()