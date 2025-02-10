from django.shortcuts import render, redirect, get_object_or_404
from todoapp1.models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todoapp1/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'todoapp1/add_task.html')

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.title = request.POST['title']
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')
    return render(request, 'todoapp1/update_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
