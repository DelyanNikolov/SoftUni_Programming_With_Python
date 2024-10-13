from django.shortcuts import render, redirect

from petstagram.pets.forms import PetAddForm, PetEditForm
from petstagram.pets.models import Pets


# Create your views here.


def pet_add(request):
    form = PetAddForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile_details', pk=1)

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-add-page.html', context)


def pet_delete(request, username: str, pet_slug: str):
    pet = Pets.objects.get(slug=pet_slug)
    form = PetEditForm(instance=pet)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile_details', pk=1)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pets/pet-delete-page.html', context)


def pet_edit(request, username: str, pet_slug: str):
    pet = Pets.objects.get(slug=pet_slug)
    form = PetEditForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('pet-details', username, pet_slug)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def pet_details(request, username: str, pet_slug: str):
    pet = Pets.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos,
    }

    return render(request, 'pets/pet-details-page.html', context)
