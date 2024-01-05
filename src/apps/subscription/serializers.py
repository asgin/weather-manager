from rest_framework import serializers
from apps.subscription.models import Subscription

class SubscribeCreateSerializer(serializers.ModelSerializer):
    send_every_hours = serializers.IntegerField(min_value=1, max_value=24)
    city = serializers.CharField(max_length=255)

    class Meta:
        model = Subscription
        fields = ('send_every_hours', 'city')


class SubscribeDeleteSerializer(serializers.ModelSerializer):
    city = serializers.CharField(max_length=255, )

    class Meta:
        model = Subscription
        fields = ('city',)