from django.db import models
import datetime

# import bcrypt
# Create your models here.
import re
from dateutil.relativedelta import relativedelta

class UserManeger(models.Manager):
    def validate_login(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        #Validate regestration
        if len(postData['first_name']) < 2:
            errors["first_name"] = "the first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "the last name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
          errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
          errors['password']="Password needs to be more than 8 charecters"
        if postData['confirm_password'] != postData['password']:
          errors['confirm_password']="Passwords don't match!"
        if User.objects.filter(email=postData['email']).exists():
          errors['email']="This email already exists, try login page instead"
        if postData['birthday'] > str(datetime.date.today()):
          errors["birthday"]= "You should be born in the past!"
        user_birthday = datetime.datetime.strptime(postData['birthday'], '%Y-%m-%d').date()
        if user_birthday > datetime.date.today() - relativedelta(years=13):
          errors["birthday"] = "You must be at least 13 years old to register."
        return errors
  
# the users table, where the first name , last name email , password are being stored 
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255) # the bcrypt password hash only.
    birthday=models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManeger()
  # liked_books = a list of books a given user likes
  # books_uploaded = a list of books uploaded by a given user

class BookManeger(models.Manager):
    def validate_book(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        #Validate registration
        if not postData['book_title']:
            errors["book_title"] = "the book title must not be empty!"
        if len(postData['descreption']) < 5:
            errors["descreption"] = "the book description must be more than 5 characters! "
        # Check if the book with the same title already exists
        book_id = postData.get('book_id', None)
        book_title = postData['book_title']
        if book_id:
            book = Book.objects.get(id=book_id)
            if book.title != book_title and Book.objects.filter(title=book_title).exists():
                errors['book_title'] = 'A book with this title already exists'
        elif Book.objects.filter(title=book_title).exists():
            errors['book_title'] = 'A book with this title already exists'
        return errors

# Books
class Book(models.Model):
  title= models.CharField(max_length=255,unique=True)
  desc=models.TextField()
  uploaded_by=models.ForeignKey(User,related_name="books_uploaded",on_delete=models.CASCADE)
  # users_who_like =models.ManyToManyField(Users,related_name="liked_books")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = BookManeger()


class AuthorManeger(models.Manager):
    def validate_author(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        #Validate registration
        if not postData['first_name']:
            errors["first_name"] = "the first name  must not be empty!"
        if not postData['last_name']:
            errors["last_name"] = "the first name  must not be empty!"            
        return errors
# Book Authors 
class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManeger()

class ReviewManeger(models.Manager):
    def validate_review(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        #Validate registration
        if not postData['review_text']:
            errors["review_text"] = "You Can't sadly add empty reviews :)"
        if  len(postData['review_text']) < 3:
            errors["review_text"] = "Also Your review should contain words, like good or bad"
        return errors
# Reviews

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
