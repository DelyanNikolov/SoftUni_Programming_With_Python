from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from main_app.custom_choices import MissionStatusChoices
from main_app.custom_managers import AstronautManager
from main_app.custom_validators import validate_only_digits
from main_app.mixins import UpdatedAtMixin


# Create your models here.
class Astronaut(UpdatedAtMixin):
    name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    phone_number = models.CharField(max_length=15, validators=[validate_only_digits], unique=True)
    is_active = models.BooleanField(default=True)
    date_of_birth = models.DateField(null=True, blank=True)
    spacewalks = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    objects = AstronautManager()


class Spacecraft(UpdatedAtMixin):
    name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    manufacturer = models.CharField(max_length=100, )
    capacity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    weight = models.FloatField(validators=[MinValueValidator(0.0)])
    launch_date = models.DateField()


class Mission(UpdatedAtMixin):
    name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=9, choices=MissionStatusChoices.choices, default=MissionStatusChoices.PLANNED)
    launch_date = models.DateField()
    spacecraft = models.ForeignKey(to=Spacecraft, on_delete=models.CASCADE)
    astronauts = models.ManyToManyField(to=Astronaut, related_name='mission_astronauts')
    commander = models.ForeignKey(to=Astronaut, on_delete=models.SET_NULL, null=True, related_name='mission_commander')
