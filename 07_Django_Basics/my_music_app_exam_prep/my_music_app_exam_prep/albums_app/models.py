from django.core.validators import MinValueValidator
from django.db import models

from my_music_app_exam_prep.albums_app.choices import AlbumGenreChoices


# Create your models here.

class Album(models.Model):
    MAX_ALBUM_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    MAX_GENRE_LENGTH = 30
    MIN_PRICE_VALUE = 0.0

    album_name = models.CharField(
        max_length=MAX_ALBUM_NAME_LENGTH,
        unique=True,
        verbose_name='Album Name',
    )

    artist = models.CharField(
        max_length=MAX_ARTIST_NAME_LENGTH,
        verbose_name='Artist',
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=AlbumGenreChoices.choices,
        verbose_name='Genre',
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Description',
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(MIN_PRICE_VALUE)
        ],
        verbose_name='Price',
    )

    owner = models.ForeignKey(
        to='profiles_app.Profile',
        on_delete=models.CASCADE,
        related_name='albums',
        verbose_name='Owner',
    )
