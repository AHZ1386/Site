from django import template
from ..models import Product
register = template.Library()

@register.inclusion_tag('partials/last_three_item.html')
def last_three_item():
     return{'last_three_items':Product.objects.order_by('-id')[:3][::-1]}
    