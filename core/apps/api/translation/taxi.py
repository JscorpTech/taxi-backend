from modeltranslation.translator import TranslationOptions, register

from ..models import CarBrandModel


@register(CarBrandModel)
class CarBrandTranslation(TranslationOptions):
    fields = [
        "name",
    ]
