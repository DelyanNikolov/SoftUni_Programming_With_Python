from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from forumApp.accounts.forms import CustomUserChangeForm, CustomUserForm
from forumApp.accounts.models import Profile

# Register your models here.
UserModel = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    fields = ('age', 'points')


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    form = CustomUserChangeForm
    add_form = CustomUserForm

    list_display = ('username', 'email',)

    fieldsets = (
        ('Credentials', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )
