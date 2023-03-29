from django.urls import path,include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # login and regestration functions
    path('',views.main_page),
    path('handle_regestration',views.handle_regestration),
    path('handle_login',views.handle_login),
    path('redirect',views.successfull),
    path('logout',views.logout),
    path('books',views.view_books_list),
    path('books/add',views.add_books_page),
    path('books/<int:book_id>',views.view_book),
    path('users/<int:review_user_id>',views.view_user_profile),
    path('addbooks',views.handle_add_book),
    path('addreview',views.add_review),
]
