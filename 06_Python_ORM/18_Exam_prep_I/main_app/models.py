from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator, MaxValueValidator
from django.db import models

from main_app.choices import MovieGenreChoices
from main_app.custom_managers import DirectorManager
from main_app.mixins import IsAwardedMixin, LastUpdatedMixin


# Create your models here.

class GeneralInfo(models.Model):
    full_name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(120)
        ]
    )

    birth_date = models.DateField(
        default='1900-01-01',
    )

    nationality = models.CharField(
        max_length=50,
        default='Unknown',
        validators=[
            MaxLengthValidator(50),
        ]
    )

    class Meta:
        abstract = True


class Director(GeneralInfo):
    years_of_experience = models.SmallIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
        ]
    )

    objects = DirectorManager()


class Actor(GeneralInfo, IsAwardedMixin, LastUpdatedMixin):
    pass


class Movie(IsAwardedMixin, LastUpdatedMixin):
    title = models.CharField(
        max_length=150,
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(150),
        ]
    )

    release_date = models.DateField()

    storyline = models.TextField(
        null=True,
        blank=True,
    )

    genre = models.CharField(
        max_length=6,
        choices=MovieGenreChoices.choices,
        default=MovieGenreChoices.OTHER,
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0),
        ]
    )

    is_classic = models.BooleanField(
        default=False,
    )

    director = models.ForeignKey(
        to=Director,
        on_delete=models.CASCADE,
    )

    starring_actor = models.ForeignKey(
        to=Actor,
        null=True,
        on_delete=models.SET_NULL,
        related_name='starring_movies'
    )

    actors = models.ManyToManyField(
        to=Actor,
    )
