from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import CarBrandModel, CarModel, TaxiModel


@admin.register(TaxiModel)
class TaxiAdmin(ModelAdmin):
    list_display = (
        "id",
        "user__first_name",
        "user__last_name",
        "user__phone",
        "balance",
    )


@admin.register(CarModel)
class CarAdmin(ModelAdmin):
    list_filter = [
        "color",
    ]
    search_fields = [
        "brand",
        "color",
        "number",
        "taxi__user__first_name",
        "taxi__user__last_name",
        "taxi__user__phone_name",
    ]
    list_display = (
        "id",
        "taxi__user__first_name",
        "taxi__user__last_name",
        "taxi__user__phone",
        "brand",
        "number",
        "color",
    )


@admin.register(CarBrandModel)
class CarbrandAdmin(ModelAdmin):
    search_fields = ["name"]
    list_display = ("id", "name")
