
from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
def route(request):
    return redirect("/blogs")

def index(request):
  return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
  return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
  return redirect('/')

def show(request,number):
  return HttpResponse(f"placeholder to display blog number {number}")

def edit(request,number):
  return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request,number):
  return redirect('/blogs')

# def json_data(request):
#     data = {
#         'title': 'This is a title',
#         'content': 'This is the content ',
#     }
#     return JsonResponse(data)