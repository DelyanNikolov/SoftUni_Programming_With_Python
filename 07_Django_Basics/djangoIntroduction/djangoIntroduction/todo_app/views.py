
from django.shortcuts import render
from djangoIntroduction.todo_app.models import Todo


# Create your views here.
def index(request):
    title_filter = request.GET.get('title_filter', '')

    tasks = Todo.objects.filter(name__icontains=title_filter)

    context = {
        'title_filter': title_filter,
        'tasks': tasks,
    }

    return render(request, 'tasks/index.html', context)

