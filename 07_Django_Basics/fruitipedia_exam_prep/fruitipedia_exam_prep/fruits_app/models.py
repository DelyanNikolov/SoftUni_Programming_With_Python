from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia_exam_prep.fruits_app.validators import OnlyLettersValidator


# Create your models here.
class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            OnlyLettersValidator(),
        ],
        unique=True,
        error_messages={
            'unique': 'This fruit name is already in use! Try a new one.'
        },
        verbose_name="Name",
    )

    image_url = models.URLField(
        verbose_name="Image URL",
    )

    description = models.TextField(
        verbose_name="Description",
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
        verbose_name="Nutrition",
    )

    owner = models.ForeignKey(
        to='profile_app.Profile',
        on_delete=models.CASCADE,
        verbose_name="Owner",
    )

