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

# Route /books
# Redirecting to the main page where a list of all the books is being shown
# recent_reviews = Review.objects.order_by('-created_at')
def view_books_list(request):
  user_id= request.session['newUser']
  user=User.objects.get(id=user_id)
  context={
          'newUser':user,
          'all_three_books':Book.objects.all().order_by("-created_at")[:3],
          'all_the_books':Book.objects.all().order_by("-created_at")[3:],
          'all_the_reviews':Review.objects.all(),  
          }
  
  return render(request, "viewbooks.html",context)

# route /books/add
# redirecting to the add books page 
def add_books_page(request):
  user_id= request.session['newUser']
  user=User.objects.get(id=user_id)
  context={
          'newUser':user,
          'all_the_authors':Author.objects.all().order_by("-created_at"),
          }
  
  
  return render(request,"addbook.html",context)

def handle_add_book(request):
    user_id = request.session['newUser']
    user = User.objects.get(id=user_id)
    book_id = None  # set default value for book_id
    if request.method == 'POST':
        # to validate more than once since all of these are in different tables
        book_errors = Book.objects.validate_book(request.POST)
        author_errors = Author.objects.validate_author(request.POST)
        review_errors = Review.objects.validate_review(request.POST)
        errors = {f'book_{key}': value for key, value in book_errors.items()}
        errors.update({f'author_{key}': value for key, value in author_errors.items()})
        errors.update({f'review_{key}': value for key, value in review_errors.items()})
        if errors:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/books/add')
        else:
            book = Book.objects.create(title=request.POST['book_title'], uploaded_by=user)
            if request.POST['author_id']:
              added_author=request.POST['author_id']
            else:
              added_author = Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
            book.authors.add(added_author)
            Review.objects.create(
                review_text=request.POST['review'],
                rating=request.POST['rating'],
                book=book,
                user=user
            )
            
            book_id = book.id  # set book_id if there are no errors
    return redirect(f'books/{book_id}' if book_id else '/books/add')



# route to view a book
def view_book(request,book_id):
  book= Book.objects.get(id=book_id)
  user_id= request.session['newUser']
  user=User.objects.get(id=user_id)
  context={
    'book_to_view':book,
    'newUser':user,
    
  }
  return render(request,"viewbook.html",context)


# route to view users profile
def view_user_profile(request):
  return render(request, "userrating.html") 

# Add a review , handle adding a review 
def add_review(request):
    user_id = request.session['newUser']
    user = User.objects.get(id=user_id)
    book_id = None  # set default value for book_id
    if request.method == 'POST':
      
      return redirect('/books/{book_id}')
    else:
      return redirect(f'/books/{book_id}')