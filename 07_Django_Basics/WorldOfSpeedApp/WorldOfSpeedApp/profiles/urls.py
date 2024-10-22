from django.urls import path

from WorldOfSpeedApp.profiles.views import ProfileCreatePage, profile_details_page, ProfileEditPage, ProfileDeletePage

urlpatterns = [
    path('create/', ProfileCreatePage.as_view(), name='create-profile'),
    path('details/', profile_details_page, name='profile-details'),
    path('edit/', ProfileEditPage.as_view(), name='edit-profile'),
    path('delete/', ProfileDeletePage.as_view(), name='delete-profile'),
]
