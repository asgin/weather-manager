from rest_framework.views import APIView
from rest_framework.request import Request
from apps.subscription.services import SubscriptionService
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class SubscriptionView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request: Request) -> Response:
        user = request.user
        if user.is_authenticated:
            city = request.data.get('city')
            send_every_hours = request.data.get('send_every_hours')
            subscribtion = SubscriptionService()
            subscribe = subscribtion.subscribe(city=city, send_every_hours=send_every_hours, user=user)
            return Response(data=subscribe['message'], status=subscribe['status'])
        else:
            return Response(data="User is not authenticated", status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request: Request) -> Response:
        user = request.user
        if user.is_authenticated:
            city = request.data.get('city')
            subscribtion = SubscriptionService()
            unsubscribe = subscribtion.unsubscribe(user=user, city=city)
            return Response(data=unsubscribe['message'], status=unsubscribe['status'])
        else:
            return Response(data="User is not authenticated", status=status.HTTP_401_UNAUTHORIZED)