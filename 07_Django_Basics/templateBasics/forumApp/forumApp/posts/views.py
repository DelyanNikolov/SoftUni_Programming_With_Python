from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from forumApp.posts.forms import PostBaseForm, PostDeleteForm
from forumApp.posts.models import Post


# Create your views here.
def index(request):
    context = {
        "my_form": "",
    }

    return render(request, 'base.html', context)


def dashboard(request):
    context = {
        "posts": Post.objects.all(),
    }

    return render(request, 'posts/dashboard.html', context)


def add_post(request):
    form = PostBaseForm(request.POST or None)  # TODO: inherit form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dash')

    context = {
        "form": form,
    }

    return render(request, 'posts/add_post.html', context)


def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)

    context = {
        "form": form,
        "post": post,
    }

    return render(request, 'posts/delete_post.html', context)


def details_post(request, pk: int):
    post = Post.objects.get(pk=pk)

    context = {
        "post": post,
    }

    return render(request, 'posts/details_post.html', context)


def edit_post(request, pk: int):
    return HttpResponse()  # TODO fix view
