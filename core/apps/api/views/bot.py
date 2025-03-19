from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from ..permissions import BotPermission
from core.apps.shared.utils.bot import get_bot
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

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
class BotView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = BotModel.objects.all()
    serializer_class = ListBotSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBotSerializer,
        "retrieve": RetrieveBotSerializer,
        "create": CreateBotSerializer,
    }


@extend_schema(tags=["botuser"])
class BotUserView(BaseViewSetMixin, ModelViewSet):
    serializer_class = ListBotUserSerializer
    permission_classes = [BotPermission]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBotUserSerializer,
        "retrieve": RetrieveBotUserSerializer,
        "create": CreateBotUserSerializer,
    }

    def get_queryset(self):
        return BotUserModel.objects.filter(bot=get_bot(self.request))
