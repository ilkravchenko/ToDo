from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task


def home(request):
    tasks = Task.objects.filter(is_competed=False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_competed=True).order_by('-updated_at')
    
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
    }
    
    return render(request, 'home.html', context=context)