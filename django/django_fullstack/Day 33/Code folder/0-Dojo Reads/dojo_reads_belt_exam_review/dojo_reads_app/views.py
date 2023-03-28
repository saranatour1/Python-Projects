from django.shortcuts import render,redirect
from django.contrib import messages

from .models import *
# Create your views here.
import bcrypt
#the main method to show the form page
def main_page(request):
  return render(request,"main.html")
edit=0
#route to handle regestration 
#route to handle regestration 

# the login section of the app
def handle_regestration(request):
    if request.method=='POST':
        errors=User.objects.validate_login(request.POST)
        if len(errors) > 0:
            for key , value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name=request.POST['first_name'],
                                last_name=request.POST['last_name'],
                                email=request.POST['email'],
                                birthday=request.POST['birthday'],
                                password_hash=pw_hash)
            newUser=User.objects.last().id
            request.session['newUser'] = newUser
            return redirect('/books')
    else:
        return redirect('/')


# Making the logged user log in to the wall app not to the success page
def successfull(request):
    if 'newUser' in request.session:
        return redirect('/books')
    else:
        return redirect('/')

# route to handle login 

def handle_login(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email']).first()
        if user:
            if bcrypt.checkpw(request.POST['password'].encode(), user.password_hash.encode()):
                request.session['newUser'] = user.id
                return redirect('/books')
            else:
                messages.error(request, 'Invalid password')
        else:
            messages.error(request, 'Invalid email')
    return redirect('/')

def logout(request):
  request.session.flush()
  return redirect('/')

def view_books_list(request):
  user_id= request.session['newUser']
  user=User.objects.get(id=user_id)
  context={
          'newUser':user,  
          }
  
  return render(request, "viewbooks.html",context)