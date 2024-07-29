from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, MaxLengthValidator
from django.db import models

from main_app.custom_choices import MovieGenreChoices
from main_app.mixins import IsAwardedMixin, LastUpdatedMixin


# Create your models here.
class BasePerson(models.Model):
    full_name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2),
        ]
    )

    birth_date = models.DateField(
        default='1900-01-01'
    )

    nationality = models.CharField(
        max_length=50,
        default='Unknown'
    )

    class Meta:
        abstract = True


class Director(BasePerson):
    years_of_experience = models.SmallIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
        ]
    )


class Actor(BasePerson, IsAwardedMixin, LastUpdatedMixin):
    pass


class Movie(IsAwardedMixin, LastUpdatedMixin):
    title = models.CharField(
        max_length=150,
        validators=[
            MinLengthValidator(5),
        ]
    )

    release_date = models.DateField()

    storyline = models.TextField(blank=True, null=True)

    genre = models.CharField(
        max_length=6,
        choices=MovieGenreChoices.choices,
        default=MovieGenreChoices.OTHER
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ]
    )

    is_classic = models.BooleanField(default=False)

    director = models.ForeignKey(to=Director, on_delete=models.CASCADE)

    starring_actor = models.ForeignKey(to=Actor, on_delete=models.SET_NULL, null=True, related_name='starring_actors')

    actors = models.ManyToManyField(to=Actor, related_name='actors')
