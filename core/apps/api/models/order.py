from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel

from core.apps.api.models.bot import BotUserModel


class LocationModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "location"
        verbose_name = _("LocationModel")
        verbose_name_plural = _("LocationModels")


class OrderModel(AbstractBaseModel):
    frm = models.ForeignKey(
        "LocationModel", verbose_name=_("from"), on_delete=models.CASCADE, related_name="frm_orders"
    )
    to = models.ForeignKey("LocationModel", verbose_name=_("to"), on_delete=models.CASCADE, related_name="to_orders")
    price = models.PositiveBigIntegerField(verbose_name=_("price"))
    user = models.ForeignKey("BotUserModel", verbose_name=_("user"), related_name="orders", on_delete=models.CASCADE)
    count = models.PositiveIntegerField(verbose_name=_("count"), default=1)
    time = models.TimeField(null=True, blank=True, verbose_name=_("time"))

    # bot
    bot = models.ForeignKey("BotModel", verbose_name=_("bot"), on_delete=models.SET_NULL, null=True, blank=True)

    # Location fields
    location_long = models.FloatField(_("Long"), null=True, blank=True)
    location_lat = models.FloatField(_("Lat"), null=True, blank=True)

    # taxi buyurtmani qaysi taksis olgani
    taxi = models.ForeignKey(
        "TaxiModel", on_delete=models.CASCADE, verbose_name=_("taxi"), related_name="orders", null=True, blank=True
    )

    def __str__(self):
        return self.user.full_name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            frm=LocationModel._create_fake(),
            to=LocationModel._create_fake(),
            price=100,
            user=BotUserModel._create_fake(),
        )

    class Meta:
        db_table = "order"
        verbose_name = _("OrderModel")
        verbose_name_plural = _("OrderModels")
