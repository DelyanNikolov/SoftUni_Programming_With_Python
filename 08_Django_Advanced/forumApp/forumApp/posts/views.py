from datetime import datetime

from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, ListView, FormView, CreateView, UpdateView, DeleteView

from forumApp.posts.forms import PostBaseForm, PostDeleteForm, SearchForm, PostCreateForm, PostEditForm, CommentFormSet
from forumApp.posts.models import Post


# Create your views here.

class IndexView(TemplateView):
    template_name = 'common/index.html'


# def index(request):
#
#     current_time = datetime.now()
#     user_info = "Hello: "
#     context = {
#         "current_time": current_time,
#         "user_info": user_info,
#     }
#
#     return render(request, 'common/index.html', context)
#

class DashboardView(ListView, FormView):
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'
    model = Post
    form_class = SearchForm
    success_url = reverse_lazy('dash')

    def get_queryset(self):
        queryset = self.model.objects.all()

        if 'posts.can_approve_posts' not in self.request.user.get_group_permissions() or not self.request.user.has_perm(
                'posts.can_approve_posts'):
            queryset = queryset.filter(approved=True)

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')
            queryset = self.queryset.filter(title__icontains=query)

        return queryset


def approve_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.approved = True
    post.save()

    return redirect(request.META.get('HTTP_REFERER'))


# def dashboard(request):
#     form = SearchForm(request.GET)
#     posts = Post.objects.all()
#
#     if request.method == "GET":
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             posts = posts.filter(title__icontains=query)
#
#     context = {
#         "posts": posts,
#         "form": form,
#     }
#
#     return render(request, 'posts/dashboard.html', context)

class AddPostView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('dash')


# def add_post(request):
#     form = PostCreateForm(request.POST or None, request.FILES or None)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('dash')
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'posts/add_post.html', context)

class DeletePostView(DeleteView, FormView):
    model = Post
    template_name = 'posts/delete_post.html'
    context_object_name = 'post'
    success_url = reverse_lazy('dash')

    form_class = PostDeleteForm

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = Post.objects.get(pk=pk)
        return post.__dict__


# def delete_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#     form = PostDeleteForm(instance=post)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('dash')
#
#     context = {
#         "form": form,
#         "post": post,
#     }
#
#     return render(request, 'posts/delete_post.html', context)


def details_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    formset = CommentFormSet(request.POST or None)
    comments = post.comments.all()

    if request.method == 'POST':
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect('details-post', pk=post.id)

    context = {
        "post": post,
        "formset": formset,
        "comments": comments,
    }

    return render(request, 'posts/details_post.html', context)


class EditPostView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'posts/edit_post.html'
    success_url = reverse_lazy('dash')

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Post, fields=('title', 'content', 'author', 'language'))
        else:
            return modelform_factory(Post, fields=('content',))

# def edit_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#
#     if request.method == 'POST':
#         form = PostEditForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('dash')
#     else:
#         form = PostEditForm(instance=post)
#
#     context = {
#         "post": post,
#         "form": form,
#     }
#
#     return render(request, "posts/edit_post.html", context)
