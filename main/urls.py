from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
		path('', MainView),
		path('data/', get_data)
]