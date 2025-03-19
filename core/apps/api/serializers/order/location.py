from rest_framework import serializers

from ...models import LocationModel


class BaseLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = [
            "id",
            "name",
        ]


class ListLocationSerializer(BaseLocationSerializer):
    class Meta(BaseLocationSerializer.Meta): ...


class RetrieveLocationSerializer(BaseLocationSerializer):
    class Meta(BaseLocationSerializer.Meta): ...


class CreateLocationSerializer(BaseLocationSerializer):
    class Meta(BaseLocationSerializer.Meta): ...
