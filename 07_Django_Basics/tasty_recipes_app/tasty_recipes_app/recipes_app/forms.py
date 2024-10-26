from django import forms

from tasty_recipes_app.recipes_app.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author']


class RecipeCreateForm(RecipeBaseForm):
    def __init__(self, *args, **kwargs):
        super(RecipeCreateForm, self).__init__(*args, **kwargs)
        self.fields['ingredients'].widget.attrs.update({'placeholder': 'ingredient1, ingredient2, ...'})
        self.fields['instructions'].widget.attrs.update({'placeholder': 'Enter detailed instructions here...'})
        self.fields['image_url'].widget.attrs.update({'placeholder': 'Optional image URL here...'})


class EditRecipeForm(RecipeBaseForm):
    pass


class DeleteRecipeForm(RecipeBaseForm):
    def __init__(self, *args, **kwargs):
        super(DeleteRecipeForm, self).__init__(*args, **kwargs)

        self.fields['cuisine_type'].widget.attrs['readonly'] = True

        for field in self.fields.values():
            field.disabled = True
    