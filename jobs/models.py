from django.db import models

# subclass of Model class
class Job(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=200)