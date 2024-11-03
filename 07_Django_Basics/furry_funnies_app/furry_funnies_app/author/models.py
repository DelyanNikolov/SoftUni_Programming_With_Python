from django.core.validators import MinLengthValidator
from django.db import models

from furry_funnies_app.common.validators import OnlyLettersValidator, PasscodeDigitsCountValidator


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            OnlyLettersValidator(),
        ],
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            OnlyLettersValidator(),
        ],
        verbose_name='Last Name',
    )

    passcode = models.CharField(
        validators=[
            PasscodeDigitsCountValidator(),
        ],
        help_text='Your passcode must be a combination of 6 digits',
        verbose_name='Passcode',
    )

    pets_number = models.PositiveSmallIntegerField(
        verbose_name='Pets Number',
    )

    info = models.TextField(
        null=True,
        blank=True,
        verbose_name='Info',
    )

    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image URL',
    )

