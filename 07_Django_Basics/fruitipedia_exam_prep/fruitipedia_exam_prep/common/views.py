from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from fruitipedia_exam_prep.fruits_app.models import Fruit


# Create your views here.
class IndexPage(TemplateView):
    template_name = 'index.html'


class DashboardPage(ListView):
    template_name = 'dashboard.html'
    model = Fruit
