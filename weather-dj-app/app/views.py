from django.shortcuts import render
import requests


# Create your views here.
def index(request):
	longitude = '51.5'
	latitude = '-0.25'
	if request.method == 'POST':
		longitude = request.POST['longitude']
		latitude = request.POST['latitude']
	url1 = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={longitude}&lon={latitude}'
	url = url1.format(longitude = longitude,latitude = latitude)
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	
	weather_data = requests.get(url,headers=headers).json()
	context = {'weather' : weather_data,
		'longitude' : longitude,
		'latitude'  : latitude
	}
	return render(request,'app/index.html',context)