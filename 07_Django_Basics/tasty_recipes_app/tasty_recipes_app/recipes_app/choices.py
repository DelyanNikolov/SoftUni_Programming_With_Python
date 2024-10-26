from django.db import models


class CuisineTypeChoices(models.TextChoices):
    FRENCH = "French", "French"
    CHINESE = "Chinese", "Chinese"
    ITALIAN = "Italian", "Italian"
    BALCAN = "Balcan", "Balcan"
    OTHER = "Other", "Other"
