from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import CarBrandModel, CarModel, TaxiModel
from ..serializers.taxi import (
    CreateCarBrandSerializer,
    CreateCarSerializer,
    CreateTaxiSerializer,
    ListCarBrandSerializer,
    ListCarSerializer,
    ListTaxiSerializer,
    RetrieveCarBrandSerializer,
    RetrieveCarSerializer,
    RetrieveTaxiSerializer,
)


@extend_schema(tags=["taxi"])
class TaxiView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TaxiModel.objects.all()
    serializer_class = ListTaxiSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTaxiSerializer,
        "retrieve": RetrieveTaxiSerializer,
        "create": CreateTaxiSerializer,
    }


@extend_schema(tags=["car"])
class CarView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = ListCarSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCarSerializer,
        "retrieve": RetrieveCarSerializer,
        "create": CreateCarSerializer,
    }


@extend_schema(tags=["car-brand"])
class CarBrandView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CarBrandModel.objects.all()
    serializer_class = ListCarBrandSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCarBrandSerializer,
        "retrieve": RetrieveCarBrandSerializer,
        "create": CreateCarBrandSerializer,
    }
