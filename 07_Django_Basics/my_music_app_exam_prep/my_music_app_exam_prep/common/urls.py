from django import views
from django.urls import path

from my_music_app_exam_prep.common.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]
