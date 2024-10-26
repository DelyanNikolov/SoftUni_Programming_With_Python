from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from tasty_recipes_app.recipes_app.models import Recipe


# Create your views here.
class HomePage(TemplateView):
    template_name = 'common/home-page.html'


class CataloguePage(ListView):
    model = Recipe
    template_name = 'common/catalogue.html'
