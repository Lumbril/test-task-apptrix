from django.contrib import admin
from django.utils.html import format_html

from api.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active']
    readonly_fields = ['preview']

    def preview(self, obj):
        return format_html(
            '<a href="/media/{0}" target="_blank">'
            '<img src="/media/{0}" height="100"></a>', obj.get_avatar()) if obj.get_avatar() else '-'
