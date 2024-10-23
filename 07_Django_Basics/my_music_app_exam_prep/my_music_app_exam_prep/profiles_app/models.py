from django.core.validators import MinLengthValidator
from django.db import models

from my_music_app_exam_prep.validators import AlphaNumericValidator


# Create your models here.

class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_USERNAME_LENGTH = 2

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_USERNAME_LENGTH),
            AlphaNumericValidator(),
        ],
        null=False,
        blank=False,
        verbose_name="Username",
    )

    email = models.EmailField(
        verbose_name="Email",

    )

    age = models.PositiveSmallIntegerField(
        verbose_name="Age",
    )
