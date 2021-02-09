from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.db.models import Avg
from json import dumps
from django.utils.timezone import localtime
import pytz

tz = pytz.timezone("Europe/Paris")

# Main view
def MainView(request):
	# Handle the visitor count
	try:
		NumberOfVisitors = Visits.objects.all()[0]
		NumberOfVisitors.Visitors += 1
		NumberOfVisitors.save()
	except:
		Visits(Visitors=1).save()

	# Handle de values to be displayed on the page
	Statistics = Stats.objects.all().order_by('-id')[0]
	IsDown = Statistics.ResponseTime >= 59

	LastCheck = Statistics.TimeStamp
	LastCheck = (LastCheck, tz).strftime("%H:%M")

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
	
	# Putting everything in a dictionnary
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

# Secondary view to handle AJAX requests
def get_data(request, request_length):
	# Variables init
	TimeStamps = []
	ResponseTime = []
	NumberOfAttempts = []

	# Making sure there is no query abuse
	if request_length>2016:
		request_length=2016
	
	# Generating the queryset
	Statistics = Stats.objects.all().order_by('id')[:request_length]

	# Looping over the queryset to process it
	for _stat in Statistics:
		Time = _stat.TimeStamp
		TimeStamps.append((Time, tz).strftime("%H:%M"))
		ResponseTime.append(_stat.ResponseTime)
		NumberOfAttempts.append(_stat.NumberOfAttempts)

	# Putting everything in a dictionnary
	data = {
		'timestamps': TimeStamps,
		'responsetime': ResponseTime,
		'numberofattempts': NumberOfAttempts
		}
	return JsonResponse(data)