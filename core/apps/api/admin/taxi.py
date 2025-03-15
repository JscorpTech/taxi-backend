from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import CarBrandModel, CarModel, TaxiModel


@admin.register(TaxiModel)
class TaxiAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(CarModel)
class CarAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(CarBrandModel)
class CarbrandAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
