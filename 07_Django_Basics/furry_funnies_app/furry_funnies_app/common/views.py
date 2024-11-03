from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from furry_funnies_app.posts.models import Post


# Create your views here.
class IndexPage(TemplateView):
    template_name = 'common/index.html'


class DashboardPage(ListView):
    model = Post
    template_name = 'common/dashboard.html'
