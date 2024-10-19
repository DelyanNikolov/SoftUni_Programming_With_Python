from django.urls import path, include

from petstagram.photos import views
from petstagram.photos.views import PhotoAddPage, PhotoEditPage, PhotoDetailsPage

urlpatterns = [
    path('add/', PhotoAddPage.as_view(), name='photo_add'),
    path('<int:pk>/', include([
        path('', PhotoDetailsPage.as_view(), name='photo_details'),
        path('edit/', PhotoEditPage.as_view(), name='photo_edit'),
        path('delete/', views.photo_delete, name='photo_delete'),
    ]))
]