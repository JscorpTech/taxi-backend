from rest_framework import serializers

from ...models import BotUserModel


class BaseBotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUserModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListBotUserSerializer(BaseBotUserSerializer):
    class Meta(BaseBotUserSerializer.Meta): ...


class RetrieveBotUserSerializer(BaseBotUserSerializer):
    class Meta(BaseBotUserSerializer.Meta): ...


class CreateBotUserSerializer(BaseBotUserSerializer):
    class Meta(BaseBotUserSerializer.Meta): ...
