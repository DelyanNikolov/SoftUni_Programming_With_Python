from django import forms

from WorldOfSpeedApp.cars.models import Car


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)

        widgets = {
            'image_url': forms.URLInput(
                attrs={'placeholder': 'https://...'}
            )
        }

        error_messages = {
            'image_url': {
                'unique': 'This image URL is already in use! Provide a new one.'
            }
        }


class CreateCarForm(BaseCarForm):
    pass


class CarEditForm(BaseCarForm):
    pass


class CarDeleteForm(BaseCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True

