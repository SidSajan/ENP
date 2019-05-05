from django.db import models
from django import forms
# Create your models here.
class NormalLogin(models.Model):
	username = models.CharField(max_length=50, unique=True)
	password = models.CharField(max_length=50)
	hash_string = models.CharField(max_length=255)
	enp_string = models.CharField(max_length=255) 


	def __str__(self):
		return self.username