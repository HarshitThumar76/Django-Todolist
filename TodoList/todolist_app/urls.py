""" TodoList App URL Configuration """

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('additem/', views.addItem, name='addItem'),
    path('iscomplete/<todo_id>', views.isComplete, name='isComplete'),
    path('deleteitem/<todo_id>', views.deleteItem, name='deleteItem'),
    path('deletecomplete/', views.deleteComplete, name='deleteComplete'),
    path('deleteallitem/', views.deleteAllItem, name='deleteAllItem'),
]
