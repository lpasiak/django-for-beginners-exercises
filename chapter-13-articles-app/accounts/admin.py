from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'age',
        'is_staff',
    ]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (None, {'fields': ('first_name', 'last_name', 'email', 'age')}),
        (None, {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (None, {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'age', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)