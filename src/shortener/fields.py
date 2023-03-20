from django.conf import settings
from rest_framework import serializers


class WithDomainField(serializers.CharField):
    """
    WithDomainField is a custom field that adds the domain to the original value.
    """

    def to_representation(self, value):
        return settings.DOMAIN + super().to_representation(value)
