from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_page),
    path('handle_regestration',views.handle_regestration),
    path('handle_login',views.handle_login),
    path('success',views.successfull),
    path('logout',views.logout),
]
