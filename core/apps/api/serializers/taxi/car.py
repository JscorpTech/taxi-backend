from rest_framework import serializers

from ...models import CarModel


class BaseCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListCarSerializer(BaseCarSerializer):
    class Meta(BaseCarSerializer.Meta): ...


class RetrieveCarSerializer(BaseCarSerializer):
    class Meta(BaseCarSerializer.Meta): ...


class CreateCarSerializer(BaseCarSerializer):
    class Meta(BaseCarSerializer.Meta): ...
