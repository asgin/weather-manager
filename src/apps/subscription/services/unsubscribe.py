from service import BaseService
from dataclasses import dataclass
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from apps.subscription.models import Subscription
from apps.weather.models import City

@dataclass
class Unsubscribe(BaseService):
    request: Request
    city: str

    def __call__(self):
        user = self.request.user
        if user.is_authenticated:
            try:
                city_model = City.objects.get(name=self.city)
            except City.DoesNotExist:
                return Response(message="City does not exist", status=status.HTTP_404_NOT_FOUND)
            Subscription.objects.filter(user=user, city=city_model).delete()
            return Response(data={"message": "Subscription deleted successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)