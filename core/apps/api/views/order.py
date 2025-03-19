from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import LocationModel, OrderModel
from ..permissions import BotUserPermission
from ..serializers.order import (
    CreateLocationSerializer,
    CreateOrderSerializer,
    ListLocationSerializer,
    ListOrderSerializer,
    RetrieveLocationSerializer,
    RetrieveOrderSerializer,
)


@extend_schema(tags=["order"])
class OrderView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = ListOrderSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {
        "create": [BotUserPermission],
    }
    action_serializer_class = {
        "list": ListOrderSerializer,
        "retrieve": RetrieveOrderSerializer,
        "create": CreateOrderSerializer,
    }


@extend_schema(tags=["location"])
class LocationView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = LocationModel.objects.all()
    serializer_class = ListLocationSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListLocationSerializer,
        "retrieve": RetrieveLocationSerializer,
        "create": CreateLocationSerializer,
    }
