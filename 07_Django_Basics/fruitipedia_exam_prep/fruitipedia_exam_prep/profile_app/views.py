from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from fruitipedia_exam_prep.profile_app.forms import ProfileCrateForm, EditProfileForm
from fruitipedia_exam_prep.profile_app.models import Profile
from fruitipedia_exam_prep.utils import get_user_obj


# Create your views here.

class CreateProfilePage(CreateView):
    model = Profile
    form_class = ProfileCrateForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('dashboard')


class DetailsProfilePage(DetailView):
    model = Profile
    template_name = 'profiles/details-profile.html'

    def get_object(self, queryset=None):
        return get_user_obj()


class EditProfilePage(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('details-profile')

    def get_object(self, queryset=None):
        return get_user_obj()


class DeleteProfilePage(DeleteView):
    template_name = 'profiles/delete-profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_user_obj()

