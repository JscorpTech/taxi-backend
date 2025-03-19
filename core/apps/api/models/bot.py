from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from functools import cached_property


class BotModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    token = models.CharField(max_length=100, verbose_name=_("Token"))
    tg_id = models.BigIntegerField(verbose_name=_("tg_id"), default=1, unique=True)

    @cached_property
    def users_count(self) -> int:
        return self.users.count()

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
            token="ssdsd",
        )

    class Meta:
        db_table = "bot"
        verbose_name = _("BotModel")
        verbose_name_plural = _("BotModels")


class BotUserModel(AbstractBaseModel):
    first_name = models.CharField(max_length=1000, verbose_name=_("First name"))
    last_name = models.CharField(max_length=1000, verbose_name=_("Last name"))
    phone = models.CharField(_("phone"), max_length=255, null=True, blank=True)
    tg_id = models.IntegerField(verbose_name=_("Tg id"))
    bot = models.ForeignKey(
        "BotModel",
        verbose_name=_("bot"),
        related_name="users",
        on_delete=models.CASCADE,
    )

    @cached_property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        return self.first_name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            first_name="sdfsd",
            last_name="fd",
            tg_id=232323,
            bot=BotModel._create_fake(),
        )

    class Meta:
        db_table = "botuser"
        verbose_name = _("BotuserModel")
        verbose_name_plural = _("BotuserModels")
