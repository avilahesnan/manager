from django.shortcuts import render


def index(request):
    return render(request, 'tasks/pages/index.html')


def task(request, id):
    return render(request, 'tasks/pages/task-view.html', context={
        'is_detail_page': True,
    })
