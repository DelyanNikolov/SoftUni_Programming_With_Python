from django import forms

from WorldOfSpeedApp.profiles.models import Profile
from django.views.generic import CreateView

from WorldOfSpeedApp.profiles.models import Profile


# Create your views here.
class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']

        widgets = {
            'password': forms.PasswordInput(),
        }

        help_texts = {
            'age': 'Age requirement: 21 years and above.'
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
