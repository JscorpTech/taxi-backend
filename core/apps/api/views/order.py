from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from ..permissions import BotUserPermission
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import OrderModel
from ..serializers.order import CreateOrderSerializer, ListOrderSerializer, RetrieveOrderSerializer


@extend_schema(tags=["order"])
class OrderView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = ListOrderSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {
        "list": [BotUserPermission],
    }
    action_serializer_class = {
        "list": ListOrderSerializer,
        "retrieve": RetrieveOrderSerializer,
        "create": CreateOrderSerializer,
    }
