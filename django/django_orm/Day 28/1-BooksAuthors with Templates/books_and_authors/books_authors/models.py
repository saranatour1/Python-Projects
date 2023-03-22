from django.core.exceptions import ValidationError
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def clean(self):
    #     if not self.title:
    #         raise ValidationError("Title field is required.")
    #     if not self.desc:
    #         raise ValidationError("Description field is required.")

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField(default="Null")
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def clean(self):
    #     if not self.first_name:
    #         raise ValidationError("First name field is required.")
    #     if not self.last_name:
    #         raise ValidationError("Last name field is required.")
