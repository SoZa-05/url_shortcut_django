from django.contrib import admin
from django.contrib.admin import ModelAdmin

from mini_url.models import MiniUrl


# Register your models here.


class UrlAdmin(ModelAdmin):
    list_display = ('url_long', 'code', 'created_at')


admin.register(MiniUrl, UrlAdmin)
