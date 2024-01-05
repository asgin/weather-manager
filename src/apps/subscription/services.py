from typing import Dict, Union
from apps.subscription.repositories.interfaces import BaseService
from apps.subscription.repositories.repository import SubscribtionRepository
from apps.subscription.tasks import send_mail_to_user
from apps.user.models import WeatherManagerUser
from config.celery_app import app
from celery.schedules import crontab
from apps.subscription.serializers import *
from rest_framework import status

class SubscriptionService(BaseService):

    def subscribe(self, city: str, send_every_hours: int, user: WeatherManagerUser) -> Dict[str, Union[str, int]]:
        data = SubscribeCreateSerializer(data={'city': city, 'send_every_hours': send_every_hours})
        if data.is_valid():
            subscribtion_repository = SubscribtionRepository()
            subscribe = subscribtion_repository.subscribe(send_every_hours=data.validated_data['send_every_hours'], city=data.validated_data['city'], user=user)
            app.add_periodic_task(
                    crontab(hour="*/{}".format(data.validated_data['send_every_hours'])),
                    send_mail_to_user.s(user.id),
                    name="send_email_to{}".format(user.id),
            )
            app.conf.beat_schedule["send_email_to{}".format(user.id)] = {
                "task": "send_mail_to_user",
                "schedule": crontab(hour="*/{}".format(data.validated_data['send_every_hours'])),
                "args": (user.id,),
            }

            return subscribe
        else:
            return {"message": f"Invalid data, error: {data.errors}", "status": status.HTTP_400_BAD_REQUEST}

    def unsubscribe(self, city: str, user: WeatherManagerUser) -> Dict[str, Union[str, int]]:
        subscribtion_repository = SubscribtionRepository()
        data = SubscribeDeleteSerializer(data={'city': city})
        if data.is_valid():
            app.conf.beat_schedule.pop("send_email_to{}".format(user.id))
            return subscribtion_repository.unsubscribe(city=data.validated_data['city'], user=user)
        else:
            return {"message": f"Invalid data, error: {data.errors}", "status": status.HTTP_400_BAD_REQUEST}
    