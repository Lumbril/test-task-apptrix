from django.contrib import admin

from api.models import Grade


@admin.register(Grade)
class UserAdmin(admin.ModelAdmin):
    list_display = ['who', 'whom', 'grade']
