from django import forms

from fruitipedia_exam_prep.profile_app.mixins import PlaceholderMixin, RemoveLabelMixin
from fruitipedia_exam_prep.profile_app.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'password']

    password = forms.CharField(widget=forms.PasswordInput)


class ProfileCrateForm(PlaceholderMixin, RemoveLabelMixin, BaseProfileForm):
    pass
