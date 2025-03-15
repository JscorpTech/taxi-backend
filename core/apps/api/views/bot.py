from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

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
class BotUserView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = BotUserModel.objects.all()
    serializer_class = ListBotUserSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBotUserSerializer,
        "retrieve": RetrieveBotUserSerializer,
        "create": CreateBotUserSerializer,
    }
