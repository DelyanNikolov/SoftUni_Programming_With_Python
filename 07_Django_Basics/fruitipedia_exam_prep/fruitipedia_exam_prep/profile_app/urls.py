from django.urls import path

from fruitipedia_exam_prep.profile_app.views import CreateProfilePage

urlpatterns = [
    path('create/', CreateProfilePage.as_view(), name='create-profile'),
]
