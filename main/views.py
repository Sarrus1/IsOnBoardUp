from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.db.models import Avg
from json import dumps

def MainView(request):
	try:
		NumberOfVisitors = Visits.objects.all()[0]
		NumberOfVisitors.Visitors += 1
		NumberOfVisitors.save()
	except:
		Visits(Visitors=1).save()

	Statistics = Stats.objects.all().order_by('-id')[0]
	IsDown = Statistics.ResponseTime >= 59
	LastCheck = Statistics.TimeStamp.strftime("%H:%M")
	AverageLoginTime = Stats.objects.exclude(ResponseTime=60.0).aggregate(Avg('ResponseTime'))["ResponseTime__avg"]
	AverageLoginTime  = round(AverageLoginTime, 1)
	AverageNumberOfRetries = Stats.objects.aggregate(Avg('NumberOfAttempts'))["NumberOfAttempts__avg"]
	AverageNumberOfRetries = round(AverageNumberOfRetries, 1)
	TotalFailed = Stats.objects.filter(ResponseTime=60.0).count()
	Total = Stats.objects.count()

	DonutData = {
			'total_failed': TotalFailed,
			'total': Total
		}
	
	data = {
		'isdown': IsDown, 
		'averagelogin': AverageLoginTime, 
		'lastcheck': LastCheck,
		'donut_data': dumps(DonutData),
		'visitors_count': NumberOfVisitors.Visitors,
		'averageretry': AverageNumberOfRetries,
		'numberofqueries': Total
		}
	
	return render(request, 'main/index.html', data)

def get_data(request, request_length):
	if request_length>2016:
		request_length=2016
	Statistics = Stats.objects.all().order_by('id')[:request_length]
	TimeStamps = []
	ResponseTime = []
	NumberOfAttempts = []
	for _stat in Statistics:
		TimeStamps.append(_stat.TimeStamp.strftime("%H:%M"))
		ResponseTime.append(_stat.ResponseTime)
		NumberOfAttempts.append(_stat.NumberOfAttempts)

	data = {
		'timestamps': TimeStamps,
		'responsetime': ResponseTime,
		'numberofattempts': NumberOfAttempts
		}
	return JsonResponse(data)