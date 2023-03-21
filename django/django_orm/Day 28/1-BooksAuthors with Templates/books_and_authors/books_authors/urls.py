from django.urls import path
from . import views
#addition of  url patterns
urlpatterns = [
    # path('admin/', admin.site.urls),
    #the main url root, that displays the addbooks.html page 
    path('',views.firstpage),
    # the add books route to proccess the  POST method of adding a book
    path('addbooks',views.addbooks),
    #show books route, to get the information of each book
    path('books/<int:number>',views.showBooks),
    # the proccess of adding an author to the book 'relationship'
    path('addAuthorsToBook',views.addRelatedAuthors),
    #get the author proccess 
    path('authors',views.showAuthors),
    # adding an author 'from the root of author'
    path('addAuthor',views.addAuthors),
    # show the author 'get method' 
    path('authors/<int:number>',views.viewAuthor),
    # the proccess of adding a book to an author 'relationship'
    path('addbooktoauthor',views.addRelatedBook)
]
