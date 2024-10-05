from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.custom_choices import ArticleCategoryChoices
from main_app.custom_managers import AuthorManager
from main_app.mixins import PublishedOnMixin


# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    email = models.EmailField(unique=True)
    is_banned = models.BooleanField(default=False)
    birth_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2005)]
    )
    website = models.URLField(null=True, blank=True)

    objects = AuthorManager()


class Article(PublishedOnMixin, models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    content = models.TextField(validators=[MinLengthValidator(10)])
    category = models.CharField(
        max_length=10,
        choices=ArticleCategoryChoices.choices,
        default=ArticleCategoryChoices.TECHNOLOGY,
    )
    authors = models.ManyToManyField(to=Author, related_name='articles_authors')


class Review(PublishedOnMixin, models.Model):
    content = models.TextField(validators=[MinLengthValidator(10)])
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    author = models.ForeignKey(to=Author, related_name='reviews_author', on_delete=models.CASCADE)
    article = models.ForeignKey(to=Article, related_name='reviews', on_delete=models.CASCADE)
