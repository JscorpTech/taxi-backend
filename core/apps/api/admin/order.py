from django.contrib import admin
from unfold.admin import ModelAdmin
from core.apps.shared.utils.user import USER_SEARCH_FIELD

from ..models import LocationModel, OrderModel


@admin.register(OrderModel)
class OrderAdmin(ModelAdmin):
    list_filter = [
        "frm",
        "to",
        "price",
    ]
    search_fields = ["frm__name", "to__name", "location_long", "location_lat"] + USER_SEARCH_FIELD
    list_display = ("id", "frm", "to", "price", "user__phone")


@admin.register(LocationModel)
class LocationAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
