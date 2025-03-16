from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.api.models.bot import BotUserModel


class OrderModel(AbstractBaseModel):
    frm = models.TextField(verbose_name=_("from"))
    to = models.TextField(verbose_name=_("to"))
    price = models.PositiveBigIntegerField(verbose_name=_("price"))
    user = models.ForeignKey("BotUserModel", verbose_name=_("user"), related_name="orders", on_delete=models.CASCADE)
    count = models.PositiveIntegerField(verbose_name=_("count"), default=1)
    time = models.TimeField(null=True, blank=True, verbose_name=_("time"))

    def __str__(self):
        return self.user.full_name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            frm="fdsf",
            to="fdf",
            price=100,
            user=BotUserModel._create_fake(),
        )

    class Meta:
        db_table = "order"
        verbose_name = _("OrderModel")
        verbose_name_plural = _("OrderModels")
