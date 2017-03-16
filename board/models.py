from django.db import models

class Employee(models.Model):

	name = models.CharField(max_length=100, blank=False)
	email = models.CharField(max_length=100, blank=False, unique=True)
	department = models.CharField(max_length=100, blank=False)

	def __str__(self):
		return self.name