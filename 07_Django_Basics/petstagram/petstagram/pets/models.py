from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.


class Pets(models.Model):
    name = models.CharField(
        max_length=30,
    )

    personal_photo = models.URLField()

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # if not self.slug: (row removed to fix slug change in url)
        self.slug = slugify(f"{self.name} - {self.id}")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
