from django.shortcuts import render,redirect
from .models import *

# the books related proccess 

# render the main page , that has the form and all the table 
def firstpage(request):
  context={
    'all_books':Book.objects.all(),
  }
  return render(request,"addbooks.html",context)
# the method to proccesss the form that adds a book to the database , and redirects to th main page 
def addbooks(request):
  Book.objects.create(title=request.POST['book_title'],desc=request.POST['descreption'])
  return redirect('/')
# render the show page , with all the elements that are in the database 
def showBooks(request,number):
  book_to_grab=Book.objects.get(id=number)
  context={
      'book_to_grab':book_to_grab,
      'all_authors':Author.objects.all(),
  }
  return render(request,"showbooks.html",context)
# the proccess of adding the relationships 'books to authors'
def addRelatedAuthors(request):
  if request.method=='POST':
    author=request.POST.get('author_id')
    book=request.POST.get('book_id')
    author_id=Author.objects.get(id=int(author)) 
    book_id = Book.objects.get(id=int(book))
    book_id.authors.add(author_id)
  return redirect(f'books/{book}')

# render the show page for viewing the authors 
def showAuthors(request):
  context={
    'all_authors':Author.objects.all(),
    }
  return render(request,"addauthors.html",context)
#the proccess of creating an author object
def addAuthors(request):
  Author.objects.create(first_name=request.POST['first_name'],
                        last_name=request.POST['last_name'],
                        notes=request.POST['notes'])
  return redirect('/authors')

# get method to view the author 
def viewAuthor(request,number):
  author_to_grab=Author.objects.get(id=number)
  context={
            'author_to_grab':author_to_grab,
            'all_books':Book.objects.all(),
          }
  return render(request,"viewauthors.html",context)

# the proccess of adding 'books to authors' again 
def addRelatedBook(request):
  if request.method=='POST':
    book=request.POST.get('book_id')
    author=request.POST.get('author_id')
    author_id=Author.objects.get(id=int(author)) 
    book_id = Book.objects.get(id=int(book))
    author_id.books.add(book_id)
  return redirect(f'authors/{author}')