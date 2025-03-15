from rest_framework import serializers

from ...models import TaxiModel


class BaseTaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxiModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListTaxiSerializer(BaseTaxiSerializer):
    class Meta(BaseTaxiSerializer.Meta): ...


class RetrieveTaxiSerializer(BaseTaxiSerializer):
    class Meta(BaseTaxiSerializer.Meta): ...


class CreateTaxiSerializer(BaseTaxiSerializer):
    class Meta(BaseTaxiSerializer.Meta): ...
