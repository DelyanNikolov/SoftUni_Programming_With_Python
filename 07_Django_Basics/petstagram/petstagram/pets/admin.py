from django.contrib import admin

from petstagram.pets.models import Pets


# Register your models here.
@admin.register(Pets)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
