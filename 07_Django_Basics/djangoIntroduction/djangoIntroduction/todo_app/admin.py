from django.contrib import admin

from djangoIntroduction.todo_app.models import Todo


# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
