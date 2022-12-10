""" TodoList App URL Configuration """

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('additem/', views.addItem, name='addItem'),
    path('deleteitem/<todo_id>', views.deleteItem, name='deleteItem'),
    path('deleteitemall/', views.deleteItemAll, name='deleteItemAll'),
]
