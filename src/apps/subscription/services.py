from apps.subscription.repositories.interfaces import BaseService
from rest_framework.request import Request
from rest_framework import status
from apps.subscription.repositories.repository import SubscribtionRepository
from apps.subscription.tasks import send_mail_to_user
from config.celery_app import app
from celery.schedules import crontab

class SubscriptionService(BaseService):

    def subscribe(self, request: Request):
        subscribtion_repository = SubscribtionRepository()
        user = request.user
        send_every_hours = int(request.data.get('send_every_hours'))
        city = request.data.get('city')
        if not 0 < send_every_hours < 25:
            return {"message": "Send every hours must be between 1 and 24", "status": status.HTTP_400_BAD_REQUEST}
        if user.is_authenticated:
            subscribe = subscribtion_repository.subscribe(send_every_hours=send_every_hours, city=city, user=user)
            app.add_periodic_task(
                    crontab(hour="*/{}".format(send_every_hours)),
                    send_mail_to_user.s(user.id),
                    name="send_email_to{}".format(user.id),
            )
            app.conf.beat_schedule["send_email_to{}".format(user.id)] = {
                "task": "send_mail_to_user",
                "schedule": crontab(hour="*/{}".format(send_every_hours)),
                "args": (user.id,),
            }

            return subscribe
        else:
            return {"message": "User is not authenticated", "status": status.HTTP_401_UNAUTHORIZED}

    def unsubscribe(self, request: Request):
        subscribtion_repository = SubscribtionRepository()
        user = request.user
        city = request.data.get('city')
        if user.is_authenticated:
            app.conf.beat_schedule.pop("send_email_to{}".format(user.id))
            return subscribtion_repository.unsubscribe(city=city, user=user)
        else:
            return {"message": "User is not authenticated", "status": status.HTTP_401_UNAUTHORIZED}
        
    