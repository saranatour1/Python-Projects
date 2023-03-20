# from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('add_dojo',views.add_dojo),
    path('add_ninja',views.add_ninja),
    path('delete_dojo',views.delete_dojo)
]
