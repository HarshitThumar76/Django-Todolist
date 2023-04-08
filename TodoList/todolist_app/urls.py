""" TodoList App URL Configuration """

from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('updateitem/<int:id>', login_required(views.UpdateItemView.as_view()), name='updateItem'),
    path('iscomplete/<todo_id>', views.IsCompleteView.as_view(url='/'), name='isComplete'),
    path('deleteitem/<todo_id>', views.DeleteItemView.as_view(), name='deleteItem'),
    path('deletecomplete/', views.DeleteCompleteView.as_view(), name='deleteComplete'),
    path('deleteallitem/', views.DeleteAllItemView.as_view(), name='deleteAllItem'),
    path('search/', views.searchItem, name='searchItem'),
    path('login/', views.UserLoginView.as_view(), name='userLogin'),
    path('logout/', views.userLogout, name='userLogout'),
    path('signup/', views.UserSignUpView.as_view(), name='userSignUp'),

    # path('', views.home, name='home'),
    # path('additem/', views.addItem, name='addItem'),
    # path('iscomplete/<todo_id>', views.isComplete, name='isComplete'),
    # path('deleteitem/<todo_id>', views.deleteItem, name='deleteItem'),
    # path('deletecomplete/', views.deleteComplete, name='deleteComplete'),
    # path('deleteallitem/', views.deleteAllItem, name='deleteAllItem'),
    # path('login/', views.userLogin, name='userLogin'),
    # path('signup/', views.userSignUp, name='userSignUp'),
]
