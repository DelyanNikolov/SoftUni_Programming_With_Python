from django.urls import path

from my_music_app_exam_prep.profiles_app.views import ProfileDetailsPage, ProfileDeletePage

urlpatterns = [
   path('details/', ProfileDetailsPage.as_view(), name='details-profile'),
   path('delete/', ProfileDeletePage.as_view(), name='delete-profile')
]
