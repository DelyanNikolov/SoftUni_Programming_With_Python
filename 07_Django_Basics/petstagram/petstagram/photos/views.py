from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoAddForm, PhotoEditForm
from petstagram.photos.models import Photo


# Create your views here.

def photo_add(request):
    form = PhotoAddForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)


def photo_edit(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, instance=photo)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('photo_details', pk)

    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, 'photos/photo-edit-page.html', context)


def photo_details(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    comments_form = CommentForm()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comments_form': comments_form,
    }
    return render(request, 'photos/photo-details-page.html', context)


def photo_delete(request, pk: int):
    Photo.objects.get(pk=pk).delete()

    return redirect('home')
