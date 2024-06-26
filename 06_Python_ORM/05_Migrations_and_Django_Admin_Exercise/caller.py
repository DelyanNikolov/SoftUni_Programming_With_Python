import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Shoe


# Create queries within functions
def create_shoe():
    Shoe.objects.create(
        brand='Addidass',
        size = 40
    )

    Shoe.objects.create(
        brand='Reebock',
        size=41
    )

    Shoe.objects.create(
        brand='Puma',
        size=44
    )


create_shoe()