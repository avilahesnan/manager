from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Task


def index(request):
    all_tasks = Task.objects.all()
    alert = datetime.now() + timedelta(days=7)
    week = alert.strftime('%Y/%m/%d')

    tasks = []
    for task in all_tasks:
        term = task.term
        converted = term.strftime('%Y/%m/%d')
        result = datetime.strptime(week, '%Y/%m/%d') - datetime.strptime(converted, '%Y/%m/%d')
        task.days_to_alert -= result.days

        if not task.is_completed and task.days_to_alert <= 7:
            tasks.append(task)

    tasks.sort(key=lambda x: x.days_to_alert)

    return render(request, 'tasks/pages/index.html', context={
        'tasks': tasks
    })


def task(request, id):
    all_tasks = Task.objects.all()
    alert = datetime.now() + timedelta(days=7)
    week = alert.strftime('%Y/%m/%d')

    tasks = []
    for task in all_tasks:
        term = task.term
        converted = term.strftime('%Y/%m/%d')
        result = datetime.strptime(week, '%Y/%m/%d') - datetime.strptime(converted, '%Y/%m/%d')
        task.days_to_alert -= result.days

        if not task.is_completed and task.days_to_alert <= 7:
            tasks.append(task)

    tasks.sort(key=lambda x: x.days_to_alert)

    return render(request, 'tasks/pages/task-view.html', context={
        'is_detail_page': True,
        'tasks': tasks
    })
