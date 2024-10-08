from django.shortcuts import render


# Create your views here.


def pet_add(request):
    return render(request, 'pets/pet-add-page.html')


def pet_delete(request, username: str, pet_slug: str):
    return render(request, 'pets/pet-delete-page.html')


def pet_edit(request, username: str, pet_slug: str):
    return render(request, 'pets/pet-edit-page.html')


def pet_details(request, username: str, pet_slug: str):
    return render(request, 'pets/pet-details-page.html')
