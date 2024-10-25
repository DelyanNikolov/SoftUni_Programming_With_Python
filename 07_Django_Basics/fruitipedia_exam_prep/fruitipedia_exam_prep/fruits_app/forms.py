from django import forms

from fruitipedia_exam_prep.fruits_app.models import Fruit
from fruitipedia_exam_prep.mixins import PlaceholderMixin, RemoveLabelMixin


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ['owner']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }


class CreateFruitForm(RemoveLabelMixin, FruitBaseForm):
    pass


class EditFruitForm(FruitBaseForm):
    pass


class DeleteFruitForm(FruitBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = True
