from django.shortcuts import render

import json
import urllib.request

# Create your views here.
def home(request):
    if request.method == "POST":

        city = request.POST["city"]

        source =  urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=953b78ec2172b63a4f5d52e617e0ce7b').read()

        list_of_data = json.loads(source)

        data ={
                'country_code':str(list_of_data['sys']['country']),
                'cor':str(list_of_data["coord"]["lon"])+" "+str(list_of_data["coord"]["lat"]),
                'temp':str(list_of_data["main"]['temp']),
                'pressure':str(list_of_data['main']["pressure"]),
                'humidity':str(list_of_data['main']['humidity']),
                'main':str(list_of_data["weather"][0]['main']),
                'description':str(list_of_data["weather"][0]['description']),
                'icon':list_of_data["weather"][0]['icon'],
                'city':city
        }

    else:
        data = {}
    return render(request, "main/weather.html", data)
