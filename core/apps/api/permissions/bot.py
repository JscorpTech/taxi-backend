from rest_framework import permissions
from rest_framework.request import Request
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import AllowAny
from ..models.bot import BotUserModel, BotModel
from core.apps.shared.utils.jwt import get_pk


class BotPermission(permissions.BasePermission):

    def __init__(self) -> None: ...

    def __call__(self, *args, **kwargs):
        return self

    def has_permission(self, request, view):
        # request.bot uchun default qiymat berish
        request.bot = None
        # token malumotlarida (claim data) dan pk olish
        pk = get_pk(request)
        if pk is None:
            return False
        # databasedan botni olish
        try:
            bot = BotModel.objects.get(pk=pk)
        except BotModel.DoesNotExist:
            return False
        request.bot = bot
        return True


class BotUserPermission(AllowAny):
    message = _("Permission denied")

    def __init__(self) -> None: ...

    def __call__(self, *args, **kwargs):
        return self

    def has_permission(self, request: Request, view):
        # request.bot uchun default qiymat berish
        request.bot_user = None
        # token malumotlarida (claim data) dan pk olish
        pk = get_pk(request)
        if pk is None:
            return False
        # databasedan botni olish
        try:
            user = BotUserModel.objects.get(pk=pk)
        except BotUserModel.DoesNotExist:
            return False
        request.bot_user = user
        return True
