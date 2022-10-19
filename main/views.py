from django.shortcuts import render

import json
import urllib.request


# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST['city']
        ''' api key might be expired use your own api_key
                    place api_key in place of appid ="your_api_key_here "  '''

        # source contain JSON data from API
        # my_api_key = 'e62a9f2f78940430078f9edc2875e66d'
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=e62a9f2f78940430078f9edc2875e66d').read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['las']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)
