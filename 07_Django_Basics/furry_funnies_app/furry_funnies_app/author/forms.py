from django import forms

from furry_funnies_app.author.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'passcode', 'pets_number']
        widgets = {
            'passcode': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter your first name...'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter your last name...'})
        self.fields['passcode'].widget.attrs.update({'placeholder': 'Enter 6 digits...'})
        self.fields['pets_number'].widget.attrs.update({'placeholder': 'Enter the number of your pets...'})


class AuthorCreateForm(AuthorBaseForm):
    pass


class AuthorEditForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'pets_number', 'info', 'image_url']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_url'].label = 'Profile Image URL'
