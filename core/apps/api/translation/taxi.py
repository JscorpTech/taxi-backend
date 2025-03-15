from modeltranslation.translator import TranslationOptions, register

from ..models import CarBrandModel


@register(CarBrandModel)
class CarbrandTranslation(TranslationOptions):
    fields = [
        "name",
    ]
