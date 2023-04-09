from modeltranslation.translator import TranslationOptions, register

from .models import Product, ProductSpecs


@register(Product)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'slug', 'text', 'description','meta_title', 'meta_description', 'meta_keyword')

@register(ProductSpecs)
class NewsTranslationOptions(TranslationOptions):
    fields = ('value',)

