from modeltranslation.translator import TranslationOptions, register

from ..models import LocationModel


@register(LocationModel)
class LocationTranslation(TranslationOptions):
    fields = [
        "name",
    ]
