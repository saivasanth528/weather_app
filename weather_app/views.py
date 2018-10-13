import requests
from django.shortcuts import render, HttpResponse
from .models import City
from .forms import *
# Create your views here.


def index(request):

    if request.method == 'POST':
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=5e93b02a5d34bdbe6a109dbeb8076919&units=metric'
        # import ipdb
        # ipdb.set_trace()

        form = CityForm()
        # cities = City.objects.all()

        city = request.POST['city']
        weather_data = []
        # for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city,
            'temperature':  r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
        context = {'weather_data': weather_data}
        return render(request, 'weather_app/weather_app.html', context)

    elif request.method == 'GET':
        return render(request, 'weather_app/weather_app.html')


