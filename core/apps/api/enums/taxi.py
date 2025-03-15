from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class CarColorChoice(TextChoices):
    RED = "red", _("red")
    GREEN = "green", _("green")
    BLACK = "black", _("black")
    WHITE = "white", _("white")
