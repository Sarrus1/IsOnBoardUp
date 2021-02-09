from django.db import models

class Stats(models.Model):
	TimeStamp = models.DateTimeField()
	ResponseTime = models.DecimalField(max_digits=5, decimal_places=1)
	NumberOfAttempts = models.IntegerField()

	def __str__(self):
		return str(self.TimeStamp) if self.TimeStamp else 'Unknown'

	class Meta:
		verbose_name_plural = "Stats"

class Visits(models.Model):
	Visitors = models.IntegerField()

	def __str__(self):
		return "Number of visitors"

	class Meta:
		verbose_name_plural = "Number of visitors"