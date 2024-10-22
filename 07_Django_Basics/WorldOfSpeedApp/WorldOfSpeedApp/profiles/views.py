from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from WorldOfSpeedApp.cars.models import Car
from WorldOfSpeedApp.profiles.forms import CreateProfileForm, EditProfileForm
from WorldOfSpeedApp.profiles.models import Profile
from WorldOfSpeedApp.utils import get_user_obj


class ProfileCreatePage(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'profile/profile-create.html'
    success_url = reverse_lazy('catalogue')


def profile_details_page(request):
    profile = Profile.objects.first()
    cars = Car.objects.filter(owner=profile)
    total_sum = sum(car.price for car in cars)

    def full_name():
        if profile.first_name and profile.last_name:
            return f'{profile.first_name} {profile.last_name}'
        if profile.first_name:
            return f'{profile.first_name}'
        if profile.last_name:
            return f'{profile.last_name}'
        return None

    context = {
        'owner': profile,
        'total_sum': total_sum,
        'full_name': full_name(),
    }
    return render(request, 'profile/profile-details.html', context)


class ProfileEditPage(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'profile/profile-edit.html'
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDeletePage(DeleteView):
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_user_obj()
