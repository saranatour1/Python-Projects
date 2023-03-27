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
            return redirect('/')
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
        user = Users.objects.filter(email=request.POST['email']).first()
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

# redirect to books , once logged in 

def books_route(request):
    if 'newUser' in request.session:
      user_id=request.session['newUser']
      user = Users.objects.get(id=user_id) 
      context={
          'newUser':user,
          # 'all_messages':Messages.objects.all().order_by("-created_at"),
      }
      return render(request, "books.html", context)
    else:
      return redirect('/')


# handle adding a book path , adding the book that is uploaded by the user straight to the favorited books
def add_books(request):
    if request.method=='POST':
        errors=Books.objects.validate_book(request.POST)
        if len(errors) > 0:
            for key , value in errors.items():
                messages.error(request,value)
            return redirect('/books')
        else:
          user_id=request.session['newUser']
          user=Users.objects.get(id=user_id)
          Books.objects.create(title=request.POST['book_title'],desc=request.POST['descreption'],uploaded_by=user)
          favorited_book=Books.objects.last()
          user.liked_books.add(favorited_book)
    return redirect('/books')