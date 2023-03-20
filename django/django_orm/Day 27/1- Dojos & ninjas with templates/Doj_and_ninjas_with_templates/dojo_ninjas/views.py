from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
  all_ninjas=0

  context={
    'all_dojos':Dojos.objects.all(),
  }
  return render(request,"index.html",context)

def add_dojo(request):
  if request.method=='POST':
    Dojos.objects.create(name=request.POST['name'],city=request.POST['city'],state=request.POST['state'])
  return redirect('/')
# ,number_of_ninjas=Dojos.objects.ninjas.count()
def add_ninja(request):
  if request.method=='POST':
    dojo_id = request.POST['dojo_select']
    dojo = Dojos.objects.get(id=dojo_id)
    Ninjas.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],dojo=dojo)
  return redirect('/')

def delete_dojo(request):
  c=request.POST['delete_val']
  dojo_to_delete=Dojos.objects.get(id=c)
  dojo_to_delete.delete()

  return redirect('/')
