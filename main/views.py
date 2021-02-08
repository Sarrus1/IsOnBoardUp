from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def MainView(request):
	IsDown = Stats.objects.all().order_by('-id')[0].ResponseTime >= 59
	print(IsDown)
	return render(request, 'main/index.html', {'IsDown': IsDown})

def get_data(request):
	Statistics = Stats.objects.all().order_by('id')[:144]
	TimeStamps = []
	ResponseTime = []
	for _stat in Statistics:
		TimeStamps.append(_stat.TimeStamp)
		ResponseTime.append(_stat.ResponseTime)
	data = {
		'timestamps': TimeStamps,
		'responsetime': ResponseTime,
	}
	return JsonResponse(data)