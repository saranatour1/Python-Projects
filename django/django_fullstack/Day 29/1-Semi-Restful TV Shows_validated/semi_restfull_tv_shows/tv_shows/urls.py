from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.main),
    path('shows',views.show),
    path('shows/new',views.addShow),
    path('addingshow',views.adding),
    path('shows/<int:shownumber>', views.showSingle),
    path('shows/<int:shownumber>/edit',views.editShow),
    path('editshow/<int:shownumber>',views.update_show),
    path('shows/<int:show_id>/destroy',views.destroy),
]
