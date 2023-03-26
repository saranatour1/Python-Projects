from django.shortcuts import render, HttpResponse, redirect
from wall_app.models import *
from login.models import *

# the main page to display all the messages, allow users to post messages as well.
def main_page(request):

    user_id=request.session['newUser']
    user = Users.objects.get(id=user_id) 
    context={
        'newUser':user,
        'all_messages':Messages.objects.all(),
        }

    return render(request, "index.html", context)


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
