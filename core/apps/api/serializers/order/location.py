from rest_framework import serializers

from ...models import LocationModel


class BaseLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListLocationSerializer(BaseLocationSerializer):
    class Meta(BaseLocationSerializer.Meta): ...


class RetrieveLocationSerializer(BaseLocationSerializer):
    class Meta(BaseLocationSerializer.Meta): ...


class CreateLocationSerializer(BaseLocationSerializer):
    class Meta(BaseLocationSerializer.Meta): ...
