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


# class ShowsManeger(models.Manager):
# 	def basic_validator(self, postData):
# 		errors = {}
# 		# add keys and values to errors dictionary for each invalid field
# 		if len(postData['title']) < 5:
# 			errors["title"] = "the show title should be more than 5 charecters"
# 		if len(postData['title']) > 255:
# 			errors['title']="You have exceeded the amount of charecters for the title!"
# 		if len(postData['network']) < 10:
# 			errors["network"] = "Network name should be more than 10 charechters"
# 		if len(postData['network'])< 10:
			
# 		return errors
    