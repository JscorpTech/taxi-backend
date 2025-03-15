from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import CarBrandModel, CarModel, TaxiModel


@receiver(post_save, sender=TaxiModel)
def TaxiSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=CarModel)
def CarSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=CarBrandModel)
def CarbrandSignal(sender, instance, created, **kwargs): ...
