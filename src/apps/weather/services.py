from apps.weather.models import Weather, City

def update_weather(weather: dict, city: City) -> Weather:
    weather_object = Weather.objects.get(city=city)
    weather_object.main_weather = weather['weather'][0]['main']
    weather_object.temp = weather['main']['temp']
    weather_object.feels_like = weather['main']['feels_like']
    weather_object.speed_wind = weather['wind']['speed']
    weather_object.save()
    return weather_object