from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import BotModel, BotUserModel


@admin.register(BotModel)
class BotAdmin(ModelAdmin):
    list_display = (
        "id",
        "users_count",
        "__str__",
    )


@admin.register(BotUserModel)
class BotUserAdmin(ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone",
        "tg_id",
    )
