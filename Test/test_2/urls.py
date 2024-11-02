from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('rec/<int:pk>', views.detail_rec, name='detail_rec'),
    path('rec/delete/<int:pk>', views.delete_rec, name='delete_rec'),
    path('rec/update/<int:pk>', views.update_rec, name='update_rec'),
]
