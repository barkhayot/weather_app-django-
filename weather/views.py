from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    cities = City.objects.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q=las%20vegas&units=imperial&appid=cc168e4d57c3161d35e8573a7e08d6a0'
    
    state = 'RW'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
     
    form = CityForm()


    
    weather_data = []
    for city in cities:

        r = requests.get(url.format(city,state)).json()
        city_weather ={
            'city':city.name,
            
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    
    context = {'weather_data':weather_data, 'form':form}

    #772eeb78e737a08931a04b86c6341c32

    #api.openweathermap.org/data/2.5/weather?q={city name},{country code}
    
    #https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=772eeb78e737a08931a04b86c6341c32?
    #Kigali, RW
    return render(request, 'index.html', context)