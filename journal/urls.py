from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-entry', views.add_entry, name='add_entry'),
]