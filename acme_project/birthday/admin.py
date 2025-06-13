"""Админ зона приложения Birthday."""
from django.contrib import admin

from .models import Birthday

admin.site.empty_value_display = '-'


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    """Администрирование записей Дней рождений."""

    list_display = ('pk', 'first_name', 'last_name', 'birthday')
    search_fields = ('first_name', 'last_name')
