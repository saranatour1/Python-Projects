from django.shortcuts import render,redirect
from django.contrib import messages

from .models import *
# Create your views here.
import bcrypt
#the main method to show the form page
def main_page(request):
  return render(request,"main.html")

#route to handle regestration 
def handle_regestration(request):
  if request.method=='POST':
    errors=Users.objects.validate_login(request.POST)
    if len(errors) > 0:
      for key , value in errors.items():
        messages.error(request,value)
      return redirect('/regestration_page')
    else:
      password = request.POST['password']
      pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
      Users.objects.create(first_name = request.POST['first_name'],
                        last_name=request.POST['last_name'],
                        email=request.POST['email'],
                        birthday=request.POST['birthday'],
                        password_hash=pw_hash)
    newUser=Users.objects.last().id
    request.session['newUser']=newUser
  return redirect('/')

# Making the logged user log in to the wall app not to the success page
def successfull(request):
    if 'newUser' not in request.session:
        return redirect('/regestration_page')
    request.session['newUser'] = Users.objects.get(id=request.session['newUser'])  # user id 
    return redirect('/wall')



# route to handle login 


def handle_login(request):
    if request.method == 'POST':
        user = Users.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password_hash.encode()):
                request.session['newUser'] = logged_user.id
                return redirect('/wall')
            else:
                messages.error(request, 'Invalid password')
        else:
            messages.error(request, 'Invalid email')
    return redirect('/regestration_page')

def logout(request):
  request.session.flush()
  return redirect('/regestration_page')
