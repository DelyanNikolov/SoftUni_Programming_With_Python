from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def home_page(request):
    return render(request, template_name='index.html')
