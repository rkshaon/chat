from django.contrib import admin

from user_api.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'name', 'is_superuser', 'is_active']
    list_filter = ['is_superuser', 'is_staff', 'is_active',]
    search_fields = ['username', 'email', 'name',]
