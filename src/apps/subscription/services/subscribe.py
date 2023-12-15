from dataclasses import dataclass
from typing import Literal
from apps.weather.models import City
from service import BaseService
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from apps.subscription.models import Subscription

@dataclass
class Subscribe(BaseService):
    request: Request
    send_every_hours: Literal[2, 6, 12]
    city: str

    def __call__(self):
        user = self.request.user
        if user.is_authenticated:
            city_model = City.objects.get_or_create(name=self.city)
            Subscription.objects.create(send_every_hours=self.send_every_hours, user=user, city=city_model[0])
            return Response(data={"message": "Subscription created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(data={"message": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)