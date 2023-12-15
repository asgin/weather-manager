from typing import Literal
from rest_framework.views import APIView
from rest_framework.request import Request
from apps.subscription.services.subscribe import Subscribe
from apps.subscription.services.unsubscribe import Unsubscribe
from dataclasses import dataclass
from rest_framework.permissions import IsAuthenticated

class SubscriptionView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request: Request):
        send_every_hours = request.data.get('send_every_hours')
        city = request.data.get('city')
        return Subscribe(request=request, send_every_hours=send_every_hours, city=city)()

    def delete(self, request: Request):
        city = request.data.get('city')
        return Unsubscribe(request=request, city=city)()