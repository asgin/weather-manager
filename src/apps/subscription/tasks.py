from apps.city.models import City
from apps.subscription.models import Subscription
from apps.user.models import WeatherManagerUser
from config.celery_app import app
from django.core.mail import get_connection, EmailMessage

@app.task()
def send_mail_to_user(user_id):
    try:
        connection = get_connection()
        connection.open()
        user = WeatherManagerUser.objects.get(id=user_id)
        city = Subscription.objects.get(user=user).city
        subject = f"Hello {user.first_name}!\nWeather information for {city.name}"
        body = f"Main weather: {city.weather_info['weather'][0]['main']}\nTemperature: {city.weather_info['main']['temp']}\nFeels like: {city.weather_info['main']['feels_like']}\nWind speed: {city.weather_info['wind']['speed']}\nHumidity: {city.weather_info['main']['humidity']}" 
        email_message = EmailMessage(subject=subject, body=body, to=[user.email], from_email="weather_manager@mail.com", connection=connection)
        connection.send_messages([email_message])
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()
    return "Success"
