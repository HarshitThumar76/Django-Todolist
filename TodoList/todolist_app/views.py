from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoListForm, TodoListSearchForm
from django.views.decorators.http import require_POST


def home(request):
    todo_items = TodoItem.objects.all().order_by('id')
    form = TodoListForm()
    search_form = TodoListSearchForm()

    data = {'todo_items': todo_items, 'form': form, 'search_form': search_form}
    return render(request, 'todolist_app/home.html', data)


def searchItem(request):
    if request.method == "GET":
        search_string = request.GET.get("search_string")
        form = TodoListForm()
        todo_items = TodoItem.objects.filter(title__icontains=search_string)
        search_form = TodoListSearchForm()

        data = {'todo_items': todo_items,
                'form': form, 'search_form': search_form, 'is_search': True}
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
