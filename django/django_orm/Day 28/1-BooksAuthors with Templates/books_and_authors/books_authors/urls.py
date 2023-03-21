from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.firstpage),
    path('addbooks',views.addbooks),
    path('books/<int:number>',views.showBooks),
    path('addAuthorsToBook',views.addRelatedAuthors),
    path('authors',views.showAuthors),
    path('addAuthor',views.addAuthors),
    path('authors/<int:number>',views.viewAuthor),
    path('addbooktoauthor',views.addRelatedBook)
]
