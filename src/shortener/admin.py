from django.contrib import admin

from src.shortener.models import URLShortener


@admin.register(URLShortener)
class URLShortenerAdmin(admin.ModelAdmin):
    list_display = ["url", "short_url"]
