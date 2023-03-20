from django.conf import settings
from django.db import models


class URLShortener(models.Model):
    url = models.URLField()
    short_url = models.CharField(unique=True, max_length=settings.UNIQUE_HASH_LENGTH)

    class Meta:
        verbose_name = "URL Shortener"
        verbose_name_plural = "URL Shorteners"

    def __str__(self):
        return f"Object #{self.id}"
