from django.shortcuts import render,HttpResponse,redirect 
from wall_app.models import * 
from login.models import *

# Create your views here.

# the main page to display all the messages,allow users to post messages as well. 
def main_page(request):
  return render(request,"index.html")


# Handle adding messages direction
def add_message(request):
  if request.metnod=='POST':
    Messages.objects.create()
  return redirect('/')

#views the page of the wall , where users can add comments and messages
def viewWall(request):
  return render(request,"thewall.html")


#handle adding a comment
def add_comment(request):
  return redirect('/wall')