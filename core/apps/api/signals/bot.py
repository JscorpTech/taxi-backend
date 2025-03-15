from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import BotModel, BotUserModel


@receiver(post_save, sender=BotModel)
def BotSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=BotUserModel)
def BotuserSignal(sender, instance, created, **kwargs): ...
