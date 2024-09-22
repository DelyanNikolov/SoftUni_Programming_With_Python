from datetime import datetime

from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "current_time": datetime.now().strftime("%I:%M %p"),
    }

    return render(request, 'base.html', context)


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to create a post 1",
                "author": "Delyan Nikolov",
                "content": "I need help creating a post",
                "created_at": datetime.now().strftime("%I:%M %p"),
            },
            {
                "title": "How to create a post 2",
                "author": "",
                "content": "I need help creating a post",
                "created_at": datetime.now().strftime("%I:%M %p"),
            },
            {
                "title": "How to create a post 3",
                "author": "Delyan Nikolov",
                "content": "",
                "created_at": datetime.now().strftime("%I:%M %p"),
            }
        ]
    }

    return render(request, 'posts/dashboard.html', context)
