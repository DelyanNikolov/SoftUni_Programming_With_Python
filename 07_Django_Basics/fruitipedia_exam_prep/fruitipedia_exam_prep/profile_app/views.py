from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from fruitipedia_exam_prep.profile_app.forms import ProfileCrateForm
from fruitipedia_exam_prep.profile_app.models import Profile


# Create your views here.

class CreateProfilePage(CreateView):
    model = Profile
    form_class = ProfileCrateForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('dashboard')
