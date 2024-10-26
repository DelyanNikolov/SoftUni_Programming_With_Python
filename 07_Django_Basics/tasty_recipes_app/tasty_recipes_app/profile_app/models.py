from django.core.validators import MinLengthValidator
from django.db import models

from tasty_recipes_app.common.validators import CapitalLetterValidator


# Create your models here.

class Profile(models.Model):
    nickname = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(2, message="Nickname must be at least 2 chars long!"),
        ],
        unique=True,
        verbose_name="Nickname",
    )

    first_name = models.CharField(
        max_length=30,
        validators=[
            CapitalLetterValidator()
        ],
        verbose_name="First Name",
    )

    last_name = models.CharField(
        max_length=30,
        validators=[
            CapitalLetterValidator()
        ],
        verbose_name="Last Name",
    )

    chef = models.BooleanField(
        default=False,
        verbose_name="Chef"
    )

    bio = models.TextField(
        blank=True,
        null=True,
        verbose_name="Bio",
    )
