from django.contrib import admin

from user_api.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'name', 'is_superuser', 'is_active']
    list_filter = ['is_superuser', 'is_staff', 'is_active',]
    search_fields = ['username', 'email', 'name',]

    def save_model(self, request, obj, form, change):
        if "password" in form.changed_data:
            obj.set_password(obj.password)

        super().save_model(request, obj, form, change)
