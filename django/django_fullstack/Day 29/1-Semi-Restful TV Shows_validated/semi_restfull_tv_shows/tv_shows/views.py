from django.shortcuts import render,redirect
from django.contrib import messages

from .models import *
# Create your views here.

# show the shows table
def main(request):
  return redirect('/shows')

# /shows route, that shows all the data
def show(request):
  context={
    'all_the_shows':Shows.objects.all(),
  }
  return render(request,'shows.html',context)

# view the form to add a new show
#the addshowsform route to render the form 
def addShow(request):
  return render(request ,'addShow.html')

# Proccessing the adding of shows 
def adding(request):
  if request.method=='POST':
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
      for key, value in errors.items():
        messages.error(request, value)
      return redirect('/shows/new')
    else:
      show=Shows.objects.create(title =request.POST['title'],
                        network=request.POST['network'],
                        release_date=request.POST['releasedate'],
                        desc=request.POST['descreption'])
      messages.success(request, "TV show has been  successfully added")
      show_id=show.id
  return redirect(f'/shows/{show_id}') # route back to /shows, to view a table of the shows.

#showSingle route to show the show with the id
def showSingle(request,shownumber):
  context={
    'show_to_view':Shows.objects.get(id=shownumber),
  }
  return render(request,"showitem.html",context)


#edit one of the shows form page 
def editShow(request,shownumber):

  context={
    "show":Shows.objects.get(id=shownumber),

  }
  return render(request, "editshow.html",context)

def update_show(request,shownumber):
  if request.method=='POST':
    errors = Shows.objects.basic_validator(request.POST, show_id=shownumber)
    if len(errors) > 0:
      for key, value in errors.items():
        messages.error(request, value)
      return redirect(f'/shows/{shownumber}/edit')
    else:
      show = Shows.objects.get(id=shownumber)
      show.title = request.POST['title']
      show.network = request.POST['network']
      show.release_date = request.POST['releasedate']
      show.descreption = request.POST['descreption']
      
      print(show.release_date)
      print(request.POST['releasedate'])
      show.save()
      messages.success(request, "TV show has been  successfully added")  
  return redirect(f'/shows/{show.id}')


# edit , delete , form proccessing 
def destroy(request,show_id):
  show_to_delete=Shows.objects.get(id=show_id)
  show_to_delete.delete()
  return redirect('/shows')
