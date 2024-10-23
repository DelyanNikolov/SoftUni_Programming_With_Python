from django.db import models


class CarTypeChoices(models.TextChoices):
    RALLY = 'Rally', 'Rally'
    OPEN_WHEEL = 'Open_Wheel', 'Open_Wheel'
    KART = 'Kart', 'Kart'
    DRAG = 'Drag', 'Drag'
    OTHER = 'Other', 'Other'