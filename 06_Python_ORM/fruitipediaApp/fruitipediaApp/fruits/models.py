from django.core.validators import MinLengthValidator
from django.db import models

from fruitipediaApp.fruits.validators import OnlyLettersValidator


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            MinLengthValidator(2),
            OnlyLettersValidator()
        ]
    )

    img_url = models.URLField()

    description = models.TextField()

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='fruits',
        null=True,
    )
