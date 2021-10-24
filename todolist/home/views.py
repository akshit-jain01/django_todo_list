from django.shortcuts import render, redirect
from .models import Task

# Create your views here.


def home(request):
    context = {"success": False, 'name': 'User'}
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        print(title, description)
        ins = Task(taskTitle=title, taskDescription=description)
        ins.save()
        context = {"success": True}
    return render(request, 'index.html', context)


def tasks(request):
    allTasks = Task.objects.all()
    # for item in allTasks:
    #     print(item.taskTitle)
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)


def update_todo(request, task_id):
    # task_id = int(task_id)
    try:
        task_id = int(task_id)
        one_item = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return redirect('index')
    # return home(request)
    return render(request, 'tasks.html', {"tasks": one_item})


def delete_todo(request, task_id):

    task_id = int(task_id)
    try:
        task_sel = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return redirect('home')
    task_sel.delete()
    context = {'deletion': True}
    return render(request, 'index.html', context)
