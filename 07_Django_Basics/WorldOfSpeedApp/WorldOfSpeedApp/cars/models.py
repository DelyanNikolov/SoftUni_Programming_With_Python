from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from WorldOfSpeedApp.cars.custom_choices import CarTypeChoices
from WorldOfSpeedApp.cars.custom_validators import YearValidator
from WorldOfSpeedApp.profiles.models import Profile


# Create your models here.

class Car(models.Model):
    MAX_TYPE_LEN = 10

    MAX_MODEL_LEN = 15
    MIN_MODEL_LEN = 1

    MIN_MODEL_YEAR = 1999
    MAX_MODEL_YEAR = 2030

    MIN_PRICE_VALUE = 1.0

    type = models.CharField(
        max_length=MAX_TYPE_LEN,
        choices=CarTypeChoices.choices,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LEN,
        validators=[
            MinLengthValidator(MIN_MODEL_LEN),
        ],
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        validators=[
            YearValidator(MIN_MODEL_YEAR, MAX_MODEL_YEAR),
        ],
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        unique=True,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(MIN_PRICE_VALUE),
        ]
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        blank=True,
        null=False,
    )
