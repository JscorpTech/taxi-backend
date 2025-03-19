from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import LocationModel, OrderModel


@receiver(post_save, sender=OrderModel)
def OrderSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=LocationModel)
def LocationSignal(sender, instance, created, **kwargs): ...
