from rest_framework import serializers
from .location import ListLocationSerializer
from ..bot.botuser import ListBotUserSerializer

from ...models import OrderModel


class BaseOrderSerializer(serializers.ModelSerializer):
    user = ListBotUserSerializer()
    frm = ListLocationSerializer()
    to = ListLocationSerializer()

    class Meta:
        model = OrderModel
        exclude = [
            "bot",
            "created_at",
            "updated_at",
        ]


class ListOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class RetrieveOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class CreateOrderSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):
        kwargs["user"] = self.context.get("request").bot_user
        return super().save(**kwargs)

    class Meta(BaseOrderSerializer.Meta):
        fields = [
            "id",
            "frm",
            "to",
            "price",
            "count",
            "time",
        ]
