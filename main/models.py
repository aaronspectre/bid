from django.db import models

class Bid(models.Model):
	name = models.CharField(max_length = 200)
	phone = models.CharField(max_length = 200)
	language = models.CharField(max_length = 10)
	source = models.IntegerField()
	status = models.CharField(max_length = 50, default = 'alive')
	product = models.CharField(max_length = 50)
	date = models.DateTimeField(auto_now = True)


	def __str__(self):
		return self.name