from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def displayUsers(request):
  return HttpResponse("placeholder to later display all the list of users")

def register(request):
  return HttpResponse("placeholder for users to create a new user record")

def login(request):
  return HttpResponse("placeholder for users to log in")

