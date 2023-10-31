from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreation, CustomUserChange
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreation
    form = CustomUserChange
    model = CustomUser
    list_display = [
        "email",
        "username",
        "bio",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields":("bio",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields":("bio",)}),)

admin.site.register(CustomUser, CustomUserAdmin)