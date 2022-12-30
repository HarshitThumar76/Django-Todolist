from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoListForm, TodoListSearchForm, LoginForm, SignUpForm
from django.views.decorators.http import require_POST
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        todo_items = TodoItem.objects.filter(user=request.user).order_by('id')
        form = TodoListForm(label_suffix='')
        search_form = TodoListSearchForm(label_suffix='')
        if len(todo_items) == 0:
            messages.warning(
                request, "You have nothing to do.Please add to do task's")
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

        if len(todo_items) == 0:
            messages.warning(request, 'No task found')
        data = {'todo_items': todo_items,
                'form': form, 'search_form': search_form}
        return render(request, 'todolist_app/home.html', data)


@login_required
@require_POST
def addItem(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        new_item = form.save(commit=False)
        new_item.user = request.user
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
    login_form = LoginForm(label_suffix='')
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST, label_suffix='')
        if signup_form.is_valid():
            signup_form.save()
            messages.success(
                request, 'Your account has been registered successfully. You can now login')
            return render(request, 'todolist_app/login.html', {'login_form': login_form})
        else:
            return render(request, 'todolist_app/signup.html', {'signup_form': signup_form})
    else:
        signup_form = SignUpForm(label_suffix='')
        return render(request, 'todolist_app/signup.html', {'signup_form': signup_form})
