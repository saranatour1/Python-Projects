from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('blogs',views.index),
    path('new',views.new),
    path('create',views.create),
    path('<int:number>/edit',views.edit),
    path('<int:number>/delete',views.destroy),
    path('',views.greetings),
    
]