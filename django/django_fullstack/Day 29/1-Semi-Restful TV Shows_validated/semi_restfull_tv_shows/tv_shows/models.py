from django.db import models 
import datetime

# Create your models here.
# Inside your app's models.py file
# imports

# Validate the Add a TV Show form to ensure all fields are populated appropriately before adding to the database.

# Display errors on the Add a TV Show form if the information is invalid.


class ShowsManeger(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		# add keys and values to errors dictionary for each invalid field
		if len(postData['title']) < 2 :
			errors["title"] = "the show title should be more than 2 charecters"
		if Shows.objects.filter(title=postData['title']).exists():
			errors["title"] = "the title already exists"
		if len(postData['network']) < 3:
			errors["network"] = "Network name should be more than 3 charechters"
		if 'description' in postData and len(postData['description']) < 10:
			errors["description"] = "The description should be at least 10 characters long."
		if postData['releasedate'] > str(datetime.date.today()):
			errors["releasedate"]= "The date for the release Year must not equal anything after Today's date!"
		return errors



class Shows(models.Model):
	title = models.CharField(max_length=255,unique=True)
	network=models.CharField(max_length=255)
	release_date=models.DateField()
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects =ShowsManeger() 




