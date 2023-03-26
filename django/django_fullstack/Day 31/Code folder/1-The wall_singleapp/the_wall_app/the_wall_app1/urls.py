from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_page),
    path('handle_regestration',views.handle_regestration),
    path('handle_login',views.handle_login),
    path('redirect',views.successfull),
    path('logout',views.logout),
    path('wall',views.main_page1),
    path('add_new_message',views.add_message),
    path('wall-and-comments',views.view_wall),
    path('add_new_comment',views.add_comment)
]
