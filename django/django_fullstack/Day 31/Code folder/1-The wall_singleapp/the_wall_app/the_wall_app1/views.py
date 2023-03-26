from django.shortcuts import render,redirect
from django.contrib import messages

from .models import *
# Create your views here.
import bcrypt
#the main method to show the form page
def main_page(request):
  return render(request,"main.html")

#route to handle regestration 
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
            Users.objects.create(first_name=request.POST['first_name'],
                                last_name=request.POST['last_name'],
                                email=request.POST['email'],
                                birthday=request.POST['birthday'],
                                password_hash=pw_hash)
            newUser=Users.objects.last().id
            request.session['newUser'] = newUser
            return redirect('/wall')
    else:
        return redirect('/')


# Making the logged user log in to the wall app not to the success page
def successfull(request):
    if 'newUser' in request.session:
        return redirect('/wall')
    else:
        return redirect('/regestration_page')

# route to handle login 

def handle_login(request):
    if request.method == 'POST':
        user = Users.objects.filter(email=request.POST['email']).first()
        if user:
            if bcrypt.checkpw(request.POST['password'].encode(), user.password_hash.encode()):
                request.session['newUser'] = user.id
                return redirect('/wall')
            else:
                messages.error(request, 'Invalid password')
        else:
            messages.error(request, 'Invalid email')
    return redirect('/regestration_page')

def logout(request):
  request.session.flush()
  return redirect('/regestration_page')


# the main page to display all the messages, allow users to post messages as well.
def main_page(request):
    if 'newUser' in request.session:
        user_id=request.session['newUser']
        user = Users.objects.get(id=user_id) 
        context={
            'newUser':user,
            'all_messages':Messages.objects.all(),
        }
        return render(request, "index.html", context)
    else:
        return redirect('/regestration_page')



# Handle adding messages direction
def add_message(request):
    if request.method == 'POST':
        user_id=request.session['newUser']
        logged_user = Users.objects.get(id=user_id)
        Messages.objects.create(message=request.POST['message'], user=logged_user)
    return redirect('/wall')


# views the page of the wall, where users can add comments and messages
def view_wall(request):
    user_id=request.session['newUser']
    user = Users.objects.get(id=user_id) 
    context={
        'newUser': user,
        'all_messages': Messages.objects.all(),
    }
    return render(request, "thewall.html", context)


# handle adding a comment
def add_comment(request):
    if request.method == 'POST':
        user_id=request.session['newUser']
        logged_user = Users.objects.get(id=user_id)
        message = Messages.objects.get(id=request.POST['message_id'])
        Comments.objects.create(comment=request.POST['comment'], user=logged_user, message=message)
    return redirect('/wall')
  
