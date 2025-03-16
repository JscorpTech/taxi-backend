from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import OrderModel


@receiver(post_save, sender=OrderModel)
def OrderSignal(sender, instance, created, **kwargs): ...
