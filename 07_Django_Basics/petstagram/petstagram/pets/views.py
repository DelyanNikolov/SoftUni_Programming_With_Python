from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetAddForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pets


# Create your views here.

class PetAddPage(CreateView):
    model = Pets
    form_class = PetAddForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile_details', kwargs={'pk': 1})


# def pet_add(request):
#     form = PetAddForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('profile_details', pk=1)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'pets/pet-add-page.html', context)


class PetDeletePage(DeleteView):
    model = Pets
    template_name = 'pets/pet-delete-page.html'
    slug_url_kwarg = 'pet_slug'
    form_class = PetDeleteForm
    success_url = reverse_lazy('profile_details', kwargs={'pk': 1})

    def get_initial(self):
        return self.get_object().__dict__  # must allways return dict

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_object(),
        })
        return kwargs


# def pet_delete(request, username: str, pet_slug: str):
#     pet = Pets.objects.get(slug=pet_slug)
#     form = PetEditForm(instance=pet)
#
#     if request.method == 'POST':
#         pet.delete()
#         return redirect('profile_details', pk=1)  # pk=1 hardcoded there are no users functionality
#
#     context = {
#         'form': form,
#         'pet': pet,
#     }
#
#     return render(request, 'pets/pet-delete-page.html', context)


class PetEditPage(UpdateView):
    model = Pets
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    form_class = PetEditForm

    def get_success_url(self):
        return reverse_lazy(
            'pet-details',
            kwargs={
                'username': self.kwargs['username'],
                'pet_slug': self.kwargs['pet_slug']
            }
        )


# def pet_edit(request, username: str, pet_slug: str):
#     pet = Pets.objects.get(slug=pet_slug)
#     form = PetEditForm(request.POST or None, instance=pet)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#
#             return redirect('pet-details', username, pet_slug)
#
#     context = {
#         'form': form,
#         'pet': pet,
#     }
#
#     return render(request, 'pets/pet-edit-page.html', context)


class PetDetailsPage(DetailView):
    model = Pets
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet'] = self.get_object()
        context['all_photos'] = context['pets'].photo_set.all()
        context['comments_form'] = CommentForm()
        return context

# def pet_details(request, username: str, pet_slug: str):
#     pet = Pets.objects.get(slug=pet_slug)
#     all_photos = pet.photo_set.all()
#     comments_form = CommentForm()
#
#     context = {
#         'pet': pet,
#         'all_photos': all_photos,
#         'comments_form': comments_form,
#     }
#
#     return render(request, 'pets/pet-details-page.html', context)
