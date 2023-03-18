from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register',views.register),
    path('users/new',views.register),
    path('login',views.login),
    path('users',views.displayUsers),
]