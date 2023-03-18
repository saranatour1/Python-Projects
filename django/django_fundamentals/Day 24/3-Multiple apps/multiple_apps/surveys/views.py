from django.shortcuts import render,HttpResponse

# Create your views here.
def display(request):
  return HttpResponse("placeholder to display all the surveys created")

def newSurvey(request):
  return HttpResponse("placeholder for users to add a new survey")

