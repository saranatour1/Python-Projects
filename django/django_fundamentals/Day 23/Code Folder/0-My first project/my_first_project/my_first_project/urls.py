"""my_first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.route),	
    path('blogs', views.index),
    path('blogs/new',views.new),
    path('blogs/create/',views.create),
    path('blogs/<number>',views.show),
    path('blogs/<number>/edit',views.edit),
    path('blogs/<number>/delete',views.destroy),
    path('blogs/json/', views.json_data, name='json_data'),
]
