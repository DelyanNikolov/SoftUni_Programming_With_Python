from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(5),
        ],
        unique=True,
        error_messages={
            'unique': 'Oops! That title is already taken. How about something fresh and fun'
        },
        verbose_name='Title',
    )

    image_url = models.URLField(
        help_text='Share your funniest furry photo URL!',
        verbose_name='Image URL',
    )

    content = models.TextField(
        verbose_name='Content',
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At',
    )

    author = models.ForeignKey(
        to='author.Author',
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Author',
    )

