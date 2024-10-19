from django.core.paginator import Paginator
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import ListView
from pyperclip import copy

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo


# Create your views here.

class HomePage(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos'  # by default is object list and photos
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(** kwargs)

        context['comments_form'] = CommentForm()
        context['search_form'] = SearchForm(self.request.GET)

        return context

    def get_queryset(self):
        queryset = super().get_queryset()  # all objects
        pet_name = self.request.GET.get('pet_name')

        if pet_name:
            queryset = queryset.filter(    # filter the objects
                tagged_pets__name__icontains=pet_name
            )

        return queryset
# def home_page(request):
#     all_photos = Photo.objects.all()
#     comments_form = CommentForm()
#     search_form = SearchForm(request.GET)
#
#     if search_form.is_valid():
#         all_photos = all_photos.filter(
#             tagged_pets__name__icontains=search_form.cleaned_data['pet_name']
#         )
#
#     photos_per_page = 1
#     paginator = Paginator(all_photos, photos_per_page)
#     page_number = request.GET.get('page')
#
#     if page_number:
#         all_photos = paginator.page(page_number)
#
#
#     context = {
#         'all_photos': all_photos,
#         'comments_form': comments_form,
#         'search_form': search_form,
#     }
#     return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id: int):
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo_id=photo_id)
        like.save()

    return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")


def copy_link_to_clipboard(request, photo_id: int):
    copy(request.META.get('HTTP_HOST') + resolve_url('photo_details', photo_id))
    # concatenate url and copies in clipboard

    return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")


def comment_functionality(request, photo_id: int):
    if request.method == "POST":
        photo = Photo.objects.get(pk=photo_id)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.to_photo = photo
            comment.save()

        return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")
