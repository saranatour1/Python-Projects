from django.urls import path
from . import views

urlpatterns = [
    path('regestration_page',views.main_page),
    path('handle_regestration',views.handle_regestration),
    path('handle_login',views.handle_login),
    path('wall',views.successfull),
    path('logout',views.logout),
    path('',views.main_page),
    path('add_new_message',views.add_message),
    path('wall',views.view_wall),
    path('add_new_comment',views.add_comment)
]
