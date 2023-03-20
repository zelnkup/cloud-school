from rest_framework.routers import DefaultRouter

from src.shortener.api.views import URLShortenerViewSet

router = DefaultRouter()

router.register("", URLShortenerViewSet, basename="shortener")


urlpatterns = router.urls
