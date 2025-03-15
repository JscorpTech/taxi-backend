from rest_framework import serializers

from ...models import CarBrandModel


class BaseCarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrandModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListCarBrandSerializer(BaseCarBrandSerializer):
    class Meta(BaseCarBrandSerializer.Meta): ...


class RetrieveCarBrandSerializer(BaseCarBrandSerializer):
    class Meta(BaseCarBrandSerializer.Meta): ...


class CreateCarBrandSerializer(BaseCarBrandSerializer):
    class Meta(BaseCarBrandSerializer.Meta): ...
