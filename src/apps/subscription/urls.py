from django.urls import path
from apps.subscription.views import SubscriptionView

urlpatterns = [
    path('subscriptions/', SubscriptionView.as_view(), name='subscriptions'),
]