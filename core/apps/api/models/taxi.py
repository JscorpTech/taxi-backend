from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel

from ..enums.taxi import CarColorChoice


class TaxiModel(AbstractBaseModel):
    user = models.OneToOneField(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE)
    balance = models.BigIntegerField(verbose_name=_("balance"))

    def __str__(self):
        return self.user.full_name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            user=get_user_model()._create_fake(),
            balance=100,
        )

    class Meta:
        db_table = "taxi"
        verbose_name = _("TaxiModel")
        verbose_name_plural = _("TaxiModels")


class CarModel(AbstractBaseModel):
    taxi = models.OneToOneField("TaxiModel", verbose_name=_("taxi"), related_name="car", on_delete=models.CASCADE)
    brand = models.ForeignKey(
        "CarBrandModel", verbose_name=_("car band"), related_name="cars", on_delete=models.CASCADE
    )
    number = models.CharField(_("number"))
    color = models.CharField(_("color"), choices=CarColorChoice.choices)

    def __str__(self):
        return self.model.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            taxi=TaxiModel._create_fake(),
            brand=CarBrandModel._create_fake(),
            number="32323",
            color=CarColorChoice.BLACK.value,
        )

    class Meta:
        db_table = "car"
        verbose_name = _("CarModel")
        verbose_name_plural = _("CarModels")


class CarBrandModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "carbrand"
        verbose_name = _("CarbrandModel")
        verbose_name_plural = _("CarbrandModels")
