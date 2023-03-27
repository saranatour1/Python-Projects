from django.urls import path,include
from . import views 
urlpatterns = [
  # Login and regestration page  page 
    path('',views.main_page),
    path('handle_regestration',views.handle_regestration),
    path('handle_login',views.handle_login),
    path('redirect',views.successfull),
    path('logout',views.logout),
    path('books',views.books_route),
    path('addbooks',views.add_books),
]
