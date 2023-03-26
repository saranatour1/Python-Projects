from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_page),
    path('add_new_message',views.add_message),
    path('wall/',views.viewWall),
    path('add_new_comment',views.add_comment)
    

]
