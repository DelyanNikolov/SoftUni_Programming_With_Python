from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from tasty_recipes_app.profile_app.forms import CreateProfileForm, EditProfileForm
from tasty_recipes_app.profile_app.models import Profile
from tasty_recipes_app.utils import get_user_obj


# Create your views here.
class CreateProfilePage(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = "profiles/create-profile.html"
    success_url = reverse_lazy('catalogue')


class DetailsProfilePage(DetailView):
    model = Profile
    template_name = "profiles/details-profile.html"

    def get_object(self, **kwargs):
        return get_user_obj()


class EditProfilePage(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = "profiles/edit-profile.html"
    success_url = reverse_lazy('details-profile')

    def get_object(self, **kwargs):
        return get_user_obj()


class DeleteProfilePage(DeleteView):
    template_name = "profiles/delete-profile.html"
    success_url = reverse_lazy('home')

    def get_object(self, **kwargs):
        return get_user_obj()
