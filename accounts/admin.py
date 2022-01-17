from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    ordering = ('-date_joined',)
    fieldsets = (
         ('Personal info', {'fields': ('email', 'password',)}),
        
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    list_display = ['first_name', 'last_name', 'email', 'city', 'image']
    readonly_fields = ("date_joined",)
    exclude = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)

