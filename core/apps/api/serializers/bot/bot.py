from rest_framework import serializers

from ...models import BotModel


class BaseBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotModel
        fields = [
            "id",
            "token",
            "tg_id",
        ]


class ListBotSerializer(BaseBotSerializer):
    class Meta(BaseBotSerializer.Meta): ...


class RetrieveBotSerializer(BaseBotSerializer):
    class Meta(BaseBotSerializer.Meta):
        fields = BaseBotSerializer.Meta.fields + [
            "name",
        ]


class CreateBotSerializer(BaseBotSerializer):
    class Meta(BaseBotSerializer.Meta): ...
