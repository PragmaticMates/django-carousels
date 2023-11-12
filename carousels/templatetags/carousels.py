from django.core.exceptions import ObjectDoesNotExist
from django import template

from carousels.models import Carousel

register = template.Library()


@register.inclusion_tag('carousels/carousel.html')
def carousel(slug):
    data = {'slug': slug}

    try:
        data['carousel'] = Carousel.objects.get(slug=slug)
    except ObjectDoesNotExist:
        pass

    return data

