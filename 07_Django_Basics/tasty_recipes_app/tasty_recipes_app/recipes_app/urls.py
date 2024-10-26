from django.urls import path, include

from tasty_recipes_app.recipes_app.views import RecipeCreatePage, RecipeDetailsPage, RecipeEditPage, RecipeDeletePage

urlpatterns = [
    path('create/', RecipeCreatePage.as_view(), name='create-recipe'),
    path('<int:recipe_id>/', include([
        path('details/', RecipeDetailsPage.as_view(), name='details-recipe'),
        path('edit/', RecipeEditPage.as_view(), name='edit-recipe'),
        path('delete/', RecipeDeletePage.as_view(), name='delete-recipe'),

    ]))
]