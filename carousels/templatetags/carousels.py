from django.contrib.staticfiles.templatetags.staticfiles import register
from django.core.exceptions import ObjectDoesNotExist

from carousels.models import Carousel


@register.inclusion_tag('carousels/carousel.html')
def carousel(slug):
    data = {'slug': slug}

    try:
        data['carousel'] = Carousel.objects.get(slug=slug)
    except ObjectDoesNotExist:
        pass

    return data

