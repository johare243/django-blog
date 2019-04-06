from django import template
from markdownx.utils import markdownify
from pages.models import Category

register = template.Library()

@register.inclusion_tag('pages/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(),
            'act_cat': cat}

@register.filter
def show_markdown(text):
    return markdownify(text)

