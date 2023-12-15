from rest_framework.test import APITestCase, APIClient
from apps.user.models import WeatherManagerUser
from apps.subscription.models import Subscription
from apps.weather.models import City
from rest_framework.authtoken.models import Token

class SubscriptionTest(APITestCase):

    def setUp(self):
        self.user = WeatherManagerUser.objects.create_user(email='2lO9o@example.com', password='test1234', username='test')
        self.city = City.objects.create(name='London')
        self.client = APIClient()
        self.token = Token.objects.create(user=self.user) 
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}') 
    
    def test_subscribe(self):
        response = self.client.post('/subscriptions/', data={'send_every_hours': 2, 'city': 'London'})
        self.assertTrue(Subscription.objects.filter(user__username='test', city__name='London', send_every_hours=2).exists())
    
    def test_unsubscribe(self):
        Subscription.objects.create(user=self.user, city=self.city, send_every_hours=2)
        self.client.delete('/subscriptions/', data={'city': 'London'})
        self.assertFalse(Subscription.objects.filter(user__email='2lO9o@example.com', city__name='London').exists())
    
