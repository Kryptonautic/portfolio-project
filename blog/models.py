from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		# name used in Django admin to display
		return self.title

	def summary(self):
		# return first 100 characters
		return self.body[:100]

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')

# Add the Blog app to the settings

# Create a migration

# Migrate

# Add to the admin