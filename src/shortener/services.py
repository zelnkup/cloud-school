import random
import string
from dataclasses import dataclass

from django.conf import settings

from src.shortener.models import URLShortener


@dataclass
class URLShortenerCreator:
    """
    URL Shortener Creator responsible for creating a unique new URL Shortener object.
    """

    validated_data: dict
    available_chars: str = string.ascii_letters + string.digits
    unique_hash_length: int = settings.UNIQUE_HASH_LENGTH

    def __call__(self) -> URLShortener:
        self.short_url = self._get_short_url()
        return self._create_object()

    def _get_hash(self) -> str:
        return "".join(
            random.choice(self.available_chars) for _ in range(self.unique_hash_length)
        )

    def _get_short_url(self) -> str:
        short_url = self._get_hash()
        if URLShortener.objects.filter(short_url=short_url).exists():
            return self._get_short_url()
        return short_url

    def _create_object(self) -> URLShortener:
        return URLShortener.objects.create(
            url=self.validated_data["url"], short_url=self.short_url
        )
