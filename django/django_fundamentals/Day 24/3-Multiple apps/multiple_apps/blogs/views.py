from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def main(request):
  return HttpResponse("Hello World!")

def index(request):
  return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
  return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
  return redirect('/blogs')

def edit(request,number):
  return  HttpResponse(f"placeholder to edit blog {number}")

def destroy(request,number):
  return redirect('/blogs')

def greetings(request):
  return redirect('/blogs')