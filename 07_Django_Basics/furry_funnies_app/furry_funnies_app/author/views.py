from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from furry_funnies_app.author.forms import AuthorCreateForm, AuthorEditForm
from furry_funnies_app.author.models import Author
from furry_funnies_app.utils import get_user_obj


# Create your views here.
class AuthorCreatePage(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'author/create-author.html'
    success_url = reverse_lazy('dashboard')


class AuthorDetailsPage(DetailView):
    template_name = 'author/details-author.html'

    def get_object(self, queryset=None):
        return get_user_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        author = get_user_obj()
        last_updated_post = author.posts.order_by('-updated_at').first()
        context['last_updated_post'] = last_updated_post

        return context


class AuthorEditPage(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'author/edit-author.html'
    success_url = reverse_lazy('author-details')

    def get_object(self, queryset=None):
        return get_user_obj()


class AuthorDeletePage(DeleteView):
    template_name = 'author/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_user_obj()
