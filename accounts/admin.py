from django.contrib import admin

from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'country')
    date_hierarchy = 'last_login'


admin.site.register(CustomUser, CustomUserAdmin)

