from django.shortcuts import render,HttpResponse

# Create your views here.

def main_page(request):
  return HttpResponse("hello")