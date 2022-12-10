from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoListForm
from django.views.decorators.http import require_POST


def home(request):
    todo_items = TodoItem.objects.all().order_by('id')
    form = TodoListForm()

    data = {'todo_items': todo_items, 'form': form}
    return render(request, 'todolist_app/home.html', data)


@require_POST
def addItem(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        new_item = TodoItem(
            title=request.POST.get('title'),
            description=request.POST.get('description')
        )
        new_item.save()
    return redirect('home')


def isComplete(request, todo_id):
    todo_item = TodoItem.objects.get(pk=todo_id)
    todo_item.is_completed = True
    todo_item.save()
    return redirect('home')


def deleteComplete(request):
    TodoItem.objects.filter(is_completed__exact=True).delete()
    return redirect('home')


def deleteItem(request, todo_id):
    TodoItem.objects.get(pk=todo_id).delete()
    return redirect('home')


def deleteAllItem(request):
    TodoItem.objects.all().delete()
    return redirect('home')
