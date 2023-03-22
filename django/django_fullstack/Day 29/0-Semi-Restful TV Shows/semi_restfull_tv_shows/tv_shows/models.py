from django.db import models

# Create your models here.
# Inside your app's models.py file
# imports
class Shows(models.Model):
	title = models.CharField(max_length=255)
	network=models.CharField(max_length=255)
	release_date=models.DateField()
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


