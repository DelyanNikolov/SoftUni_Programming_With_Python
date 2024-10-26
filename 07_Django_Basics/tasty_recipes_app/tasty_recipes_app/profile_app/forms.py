from django import forms

from tasty_recipes_app.profile_app.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["nickname", "first_name", "last_name", "chef"]


class CreateProfileForm(ProfileBaseForm):
    pass


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
