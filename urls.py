from django.urls import path
from weatherapp.views import *

urlpatterns = [
	path('', home, name = "home"),
	path('news/', news, name = "news"),
	path('contact/', contact, name = "contact"),
	path('live_cameras/', live_cameras, name = "live_cameras"),
	path('photos/', photos, name = "photos"),


]