from rest_framework import serializers

from src.shortener.fields import WithDomainField
from src.shortener.models import URLShortener
from src.shortener.services import URLShortenerCreator


class URLShortenerSerializer(serializers.ModelSerializer):
    short_url = WithDomainField(read_only=True)

    class Meta:
        model = URLShortener
        fields = ("id", "url", "short_url")

    def create(self, validated_data: dict):
        return URLShortenerCreator(validated_data)()
