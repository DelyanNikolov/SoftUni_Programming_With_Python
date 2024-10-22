from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models


# Create your models here.

class Profile(models.Model):
    MAX_LEN_USERNAME = 15
    MIN_LEN_USERNAME = 3
    MIN_LEN_USERNAME_ERROR_MSG = f'Username must be at least {MIN_LEN_USERNAME} characters long'
    USERNAME_SYMBOLS = r'^[\w]+$'  # Only letters, digits, and underscores,
    USERNAME_SYMBOLS_ERROR_MSG = 'Username must contain only letters, digits, and underscores!'

    MIN_AGE = 21

    MAX_PASSWORD_LENGTH = 20

    FIRST_NAME_MAX_LENGTH = 25
    LAST_NAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=[
            MinLengthValidator(MIN_LEN_USERNAME, message=MIN_LEN_USERNAME_ERROR_MSG),
            RegexValidator(
                regex=USERNAME_SYMBOLS,
                message=USERNAME_SYMBOLS_ERROR_MSG)
        ],
        blank=False,
        null=False,
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        validators=[
            MinValueValidator(MIN_AGE),
        ],
        blank=False,
        null=False,
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        blank=True,
        null=True,

        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        blank=True,
        null=True,
        verbose_name='Last Name',
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name='Profile Picture',
    )
