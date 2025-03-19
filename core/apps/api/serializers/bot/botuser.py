from rest_framework import serializers

from ...models import BotUserModel
from .bot import ListBotSerializer
from core.apps.shared.utils.bot import get_bot
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext as _


class BaseBotUserSerializer(serializers.ModelSerializer):
    bot = ListBotSerializer()

    class Meta:
        model = BotUserModel
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone",
            "tg_id",
            "bot",
        ]


class ListBotUserSerializer(BaseBotUserSerializer):
    class Meta(BaseBotUserSerializer.Meta): ...


class RetrieveBotUserSerializer(BaseBotUserSerializer):
    class Meta(BaseBotUserSerializer.Meta): ...


class CreateBotUserSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        if self.instance:
            return attrs
        if BotUserModel.objects.filter(tg_id=attrs["tg_id"], bot=get_bot(self.context.get("request"))).exists():
            raise ValidationError({"tg_id": _("user already")})
        return attrs

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
