from django.shortcuts import render


# Create your views here.

def photo_add(request):
    return render(request, 'photos/photo-add-page.html')


def photo_edit(request, pk: int):
    return render(request, 'photos/photo-edit-page.html')


def photo_details(request, pk: int):
    return render(request, 'photos/photo-details-page.html')
