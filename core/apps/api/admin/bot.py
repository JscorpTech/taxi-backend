from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import BotModel, BotUserModel


@admin.register(BotModel)
class BotAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(BotUserModel)
class BotuserAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
