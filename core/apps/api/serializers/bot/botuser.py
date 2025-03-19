from rest_framework import serializers

from ...models import BotUserModel
from core.apps.shared.utils.bot import get_bot


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

    def create(self, validated_data):
        validated_data["bot"] = get_bot(self.context.get("request"))
        return super().create(validated_data)

    class Meta(BaseBotUserSerializer.Meta):
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone",
            "tg_id",
        ]
