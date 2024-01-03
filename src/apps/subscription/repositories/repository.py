from apps.subscription.models import Subscription
from apps.subscription.repositories.interfaces import BaseService
from apps.city.models import City
from rest_framework.request import Request
from rest_framework import status
from typing import Dict, Union
from apps.user.models import WeatherManagerUser
        

class SubscribtionRepository(BaseService):

    def subscribe(self, send_every_hours: int, city: str, user: WeatherManagerUser) -> Dict[str, Union[str, int]]:
        city_model = City.objects.get_or_create(name=city)
        Subscription.objects.create(send_every_hours=send_every_hours, user=user, city=city_model[0])
        return {"message": "Subscription created successfully", "status": status.HTTP_201_CREATED}
        
    def unsubscribe(self, city: str, user: WeatherManagerUser) -> Dict[str, Union[str, int]]:
        try:
            city_model = City.objects.get(name=city)
        except City.DoesNotExist:
            return {"message": "City does not exist", "status": status.HTTP_404_NOT_FOUND}
        Subscription.objects.filter(user=user, city=city_model).delete()
        return {"message": "Subscription deleted successfully", "status": status.HTTP_200_OK}