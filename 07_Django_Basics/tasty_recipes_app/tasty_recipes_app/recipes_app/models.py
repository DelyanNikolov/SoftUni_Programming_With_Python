from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from tasty_recipes_app.recipes_app.choices import CuisineTypeChoices


# Create your models here.

class Recipe(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        validators=[
            MinLengthValidator(10),
        ],
        error_messages={
            'unique': "We already have a recipe with the same title!",
        },
        verbose_name="Title",
    )

    cuisine_type = models.CharField(
        max_length=7,
        choices=CuisineTypeChoices.choices,
        verbose_name="Cuisine Type",
    )

    ingredients = models.TextField(
        help_text="Ingredients must be separated by a comma and space.",
        verbose_name="Ingredients",
    )

    instructions = models.TextField(
        verbose_name="Instructions",
    )

    cooking_time = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
        ],
        help_text="Provide the cooking time in minutes.",
        verbose_name="Cooking Time",
    )

    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Image URL",
    )

    author = models.ForeignKey(
        to='profile_app.Profile',
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name="Author",
    )
