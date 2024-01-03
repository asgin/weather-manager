from rest_framework.views import APIView
from rest_framework.request import Request
from apps.subscription.services import SubscriptionService
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class SubscriptionView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request: Request) -> Response:
        subscribtion = SubscriptionService()
        subscribe = subscribtion.subscribe(request=request)
        return Response(data=subscribe['message'], status=subscribe['status'])

    def delete(self, request: Request) -> Response:
        subscribtion = SubscriptionService()
        unsubscribe = subscribtion.unsubscribe(request=request)
        return Response(data=unsubscribe['message'], status=unsubscribe['status'])