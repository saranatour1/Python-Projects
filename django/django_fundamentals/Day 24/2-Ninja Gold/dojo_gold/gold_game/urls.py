# from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('process_money',views.process_money),
    path('destroy_session',views.clear_session)
]