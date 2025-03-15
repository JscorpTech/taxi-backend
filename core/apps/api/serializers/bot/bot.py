from rest_framework import serializers

from ...models import BotModel


class BaseBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListBotSerializer(BaseBotSerializer):
    class Meta(BaseBotSerializer.Meta): ...


class RetrieveBotSerializer(BaseBotSerializer):
    class Meta(BaseBotSerializer.Meta): ...


class CreateBotSerializer(BaseBotSerializer):
    class Meta(BaseBotSerializer.Meta): ...
