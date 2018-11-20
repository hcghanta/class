import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=6101fbe909cd83818d60b85b22a349e9'


    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()


    cities = City.objects.all()

    weather_data = []

    for city in cities:
        response = requests.get(url.format(city)).json()
        weather_details = {
            'city': city.name,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon':response['weather'][0]['icon'],


        }

        weather_data.append(weather_details)

    context = {'weather_data': weather_data,'form':form}
    return render(request, 'weather/weather.html', context)

