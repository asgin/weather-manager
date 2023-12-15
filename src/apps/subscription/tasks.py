from apps.subscription.models import Subscription
from config.celery_app import app
from django.core.mail import get_connection, EmailMessage
from apps.weather.models import Weather

@app.task()
def send_weather_info_every_2_hours():
    subscriptions =[
        {
            'user': elem[0],
            'city': elem[1].name,
        }
        for elem in Subscription.objects.filter(send_every_hours=2).values_list('user', 'city')
    ]
    send_mail_to_subscribers.delay(subscriptions)
    return "Success"

@app.task()
def send_weather_info_every_6_hours():
    subscriptions =[
        {
            'user': elem[0],
            'city': elem[1].name,
        }
        for elem in Subscription.objects.filter(send_every_hours=6).values_list('user', 'city')
    ]
    send_mail_to_subscribers.delay(subscriptions)
    return "Success"

@app.task()
def send_weather_info_every_12_hours():
    subscriptions =[
        {
            'user': elem[0],
            'city': elem[1].name,
        }
        for elem in Subscription.objects.filter(send_every_hours=12).values_list('user', 'city')
    ]
    send_mail_to_subscribers.delay(subscriptions)
    return "Success"

@app.task()
def send_mail_to_subscribers(subscriptions: list):
    try:
        connection = get_connection()
        connection.open()
        email_messages = []

        for elem in subscriptions:
            try:
                weather = Weather.objects.get(city=elem['city'])
            except Weather.DoesNotExist:
                return "This city does not exist"

            subject = f"Hello {elem['user'].first_name}!\nWeather information for {elem['city']}"
            body = f"Main weather: {weather.main_weather}\nTemperature: {weather.temp}\nFeels like: {weather.feels_like}\nWind speed: {weather.speed_wind}"
            message = EmailMessage(subject=subject, body=body, to=[elem['user'].email], from_email="weather_manager@mail.com", connection=connection)
            email_messages.append(message)

        connection.send_messages(email_messages)
    except Exception as e:
        # Обработка ошибок, например, логирование
        print(f"An error occurred: {e}")
    finally:
        connection.close()
    return "Success"
