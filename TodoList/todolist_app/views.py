from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoListForm, TodoListSearchForm, LoginForm, SignUpForm
from django.views.decorators.http import require_POST
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        todo_items = TodoItem.objects.filter(user=request.user).order_by('id')
        form = TodoListForm(label_suffix='')
        search_form = TodoListSearchForm(label_suffix='')
        data = {'todo_items': todo_items,
                'form': form, 'search_form': search_form}
        return render(request, 'todolist_app/home.html', data)

    else:
        login_form = LoginForm(label_suffix='')
        return render(request, 'todolist_app/login.html', {'login_form': login_form})


@login_required
def searchItem(request):
    if request.method == "GET":
        search_string = request.GET.get("search_string")
        form = TodoListForm(label_suffix='')
        todo_items = TodoItem.objects.filter(
            title__icontains=search_string, user=request.user)
        search_form = TodoListSearchForm(label_suffix='')
        login_form = LoginForm(label_suffix='')
        signup_form = SignUpForm(label_suffix='')

        data = {'todo_items': todo_items, 'is_search': True, 'signup_form': signup_form,
                'form': form, 'search_form': search_form, 'login_form': login_form}
        return render(request, 'todolist_app/home.html', data)


@login_required
@require_POST
def addItem(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        new_item = TodoItem(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            user=request.user
        )
        new_item.save()
    return redirect('home')


@login_required
def isComplete(request, todo_id):
    todo_item = TodoItem.objects.get(pk=todo_id)
    todo_item.is_completed = True
    todo_item.save()
    return redirect('home')


@login_required
def deleteComplete(request):
    TodoItem.objects.filter(is_completed__exact=True).delete()
    return redirect('home')


@login_required
def deleteItem(request, todo_id):
    TodoItem.objects.get(pk=todo_id).delete()
    return redirect('home')


@login_required
def deleteAllItem(request):
    TodoItem.objects.filter(user=request.user).delete()
    return redirect('home')


def userLogin(request):
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    else:
        return render(request, 'todolist_app/login.html', {'login_form': login_form})


@login_required
def userLogout(request):
    logout(request)
    return redirect('home')


def userSignUp(request):
    signup_form = SignUpForm(request.POST, label_suffix='')
    login_form = LoginForm(label_suffix='')
    if signup_form.is_valid():
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password == password_confirm:
            new_user = User.objects.create_user(
                username=username, password=password
            )
            new_user.first_name = firstname
            new_user.last_name = lastname
            new_user.email = email
            new_user.save()
            return render(request, 'todolist_app/login.html', {'login_form': login_form, 'is_signup': True})
    else:
        return render(request, 'todolist_app/signup.html', {'signup_form': signup_form})
