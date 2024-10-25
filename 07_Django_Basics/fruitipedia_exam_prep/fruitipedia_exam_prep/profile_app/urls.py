from django.urls import path

from fruitipedia_exam_prep.profile_app.views import CreateProfilePage, DetailsProfilePage, EditProfilePage, \
    DeleteProfilePage

urlpatterns = [
    path('create/', CreateProfilePage.as_view(), name='create-profile'),
    path('details/', DetailsProfilePage.as_view(), name='details-profile'),
    path('edit/', EditProfilePage.as_view(), name='edit-profile'),
    path('delete/', DeleteProfilePage.as_view(), name='delete-profile'),
]
