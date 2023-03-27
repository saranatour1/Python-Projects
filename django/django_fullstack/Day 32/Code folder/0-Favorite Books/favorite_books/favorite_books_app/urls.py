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
    path('add-to-favorites/<int:book_id>',views.add_to_favorites),
    path('remove-from-favorites/<int:book_id>',views.remove_from_favorites),
    path('books/<int:book_id>',views.view_book)
]
