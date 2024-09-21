from datetime import datetime

from django.shortcuts import render


# Create your views here.
def index(request):

    context = {
        "current_time": datetime.now().strftime("%I:%M %p"),
    }

    return render(request, 'base.html', context)
