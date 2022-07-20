from django.shortcuts import render
import requests
from .models import *


# Create your views here.
def home(request):
	city = request.GET.get('city')
	url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=76376bab582797c2cc41fa116f63db4f'
	data = requests.get(url).json()
	print(data)

	tem = round((data['main']['temp']-273), 2)
	citi = data['name']
	return render(request, 'index.html', {"temp":tem, 'citi':citi})


def news(request):
	return render(request, 'news.html', {})

def live_cameras(request):
	return render(request, 'live-cameras.html', {})

def photos(request):
	return render(request, 'photos.html', {})


def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		msg = request.POST.get('msg')
		web = request.POST.get('web')
		comp_name = request.POST.get('c_name')
		print(name,email,msg,web ,comp_name )
		user = Contact(name =name , email =email , website =web ,company_name =comp_name ,message = msg)
		user.save()
	return render(request, 'contact.html', {})













