from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from tasty_recipes_app.recipes_app.forms import RecipeCreateForm, EditRecipeForm, DeleteRecipeForm
from tasty_recipes_app.recipes_app.models import Recipe
from tasty_recipes_app.utils import get_user_obj


# Create your views here.
class RecipeCreatePage(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = "recipes/create-recipe.html"
    success_url = reverse_lazy("catalogue")

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)


class RecipeDetailsPage(DetailView):
    model = Recipe
    template_name = "recipes/details-recipe.html"
    pk_url_kwarg = "recipe_id"


class RecipeEditForm:
    pass


class RecipeEditPage(UpdateView):
    model = Recipe
    form_class = EditRecipeForm
    pk_url_kwarg = "recipe_id"
    template_name = "recipes/edit-recipe.html"
    success_url = reverse_lazy("catalogue")


class RecipeDeletePage(DeleteView):
    model = Recipe
    form_class = DeleteRecipeForm
    pk_url_kwarg = "recipe_id"
    template_name = "recipes/delete-recipe.html"
    success_url = reverse_lazy("catalogue")

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
