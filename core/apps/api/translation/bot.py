from modeltranslation.translator import TranslationOptions, register

from ..models import BotModel


@register(BotModel)
class BotTranslation(TranslationOptions):
    fields = []
