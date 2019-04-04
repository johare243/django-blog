from django import template
from pages.models import Category

register = template.Library()

@register.inclusion_tag('pages/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(),
            'act_cat': cat}
