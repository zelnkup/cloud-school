from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from src.shortener.api.serializers import URLShortenerSerializer
from src.shortener.models import URLShortener


class URLShortenerViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    GenericViewSet,
):
    serializer_class = URLShortenerSerializer
    permission_classes = (AllowAny,)
    queryset = URLShortener.objects.all()
    lookup_field = "short_url"
