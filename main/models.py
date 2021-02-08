from django.db import models

class Stats(models.Model):
	TimeStamp = models.TextField()
	ResponseTime = models.DecimalField(max_digits=5, decimal_places=1)

	def __str__(self):
		return str(self.TimeStamp) if self.TimeStamp else 'Unknown'

	class Meta:
		verbose_name_plural = "Stats"
