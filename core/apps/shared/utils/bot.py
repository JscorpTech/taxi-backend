from rest_framework.exceptions import PermissionDenied
from typing import Optional
from core.apps.api.models.bot import BotModel


def get_bot(request, raise_exception=True) -> Optional[BotModel]:
    """
    Get Bot object from request in
    """
    if request is not None:
        if hasattr(request, "bot"):
            return request.bot
    if raise_exception:
        raise PermissionDenied("request in bot not found")
    return None
