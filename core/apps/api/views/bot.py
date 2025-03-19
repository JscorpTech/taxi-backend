from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from ..permissions import BotPermission
from core.apps.shared.utils.bot import get_bot
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.exceptions import NotFound
from django.utils.translation import gettext as _

from ..models import BotModel, BotUserModel
from ..serializers.bot import (
    CreateBotSerializer,
    CreateBotUserSerializer,
    ListBotSerializer,
    ListBotUserSerializer,
    RetrieveBotSerializer,
    RetrieveBotUserSerializer,
)


@extend_schema(tags=["bot"])
class BotView(BaseViewSetMixin, RetrieveModelMixin, GenericViewSet):
    queryset = BotModel.objects.all()
    serializer_class = ListBotSerializer
    permission_classes = [BotPermission]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBotSerializer,
        "retrieve": RetrieveBotSerializer,
        "create": CreateBotSerializer,
    }

    def get_object(self):
        queryset = self.get_queryset().filter(tg_id=self.kwargs.get("pk"))
        if queryset.exists():
            return queryset.first()
        raise NotFound(_("Bot not found"))


@extend_schema(tags=["botuser"])
class BotUserView(BaseViewSetMixin, ModelViewSet):
    serializer_class = ListBotUserSerializer
    permission_classes = [BotPermission]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBotUserSerializer,
        "retrieve": RetrieveBotUserSerializer,
        "create": CreateBotUserSerializer,
        "update": CreateBotUserSerializer,
        "partial_update": CreateBotUserSerializer,
    }

    def get_queryset(self):
        return BotUserModel.objects.filter(bot=get_bot(self.request))
