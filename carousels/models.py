import json

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _, pgettext_lazy


class Carousel(models.Model):
    example_settings = """
        {
            items: 1,
            loop: true,
            dots: false,
            nav: true,
            responsiveClass: true,
            animateOut: 'fadeOut',
            autoplay: true,
            autoplayHoverPause: true,
            autoplayTimeout: 5000,
            smartSpeed: 1000,
            fluidSpeed: 1000,
            autoplaySpeed: 1000,
            slideTransition: 'linear',
            center: true,
            responsive: {
                0: {
                    items: 1,
                },
                576: {
                    items: 2,
                },
                768: {
                    items: 2.5,
                },
                992: {
                    items: 3,
                },
                1200: {
                    items: 4.75,
                }
            }
        }
    """
    slug = models.SlugField(verbose_name=_('identifier'), help_text=_('slug'), unique=True, max_length=20)
    settings = JSONField(verbose_name=_('settings'), blank=True, default=dict,
                         help_text=_("For example: %s") % example_settings)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = _('carousel')
        verbose_name_plural = _('carousels')

    @property
    def settings_as_json(self):
        return json.dumps(self.settings)


class Slide(models.Model):
    carousel = models.ForeignKey(to=Carousel, verbose_name=_('carousel'), on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(pgettext_lazy('sequence/order', 'position'), default=0)
    title = models.CharField(_('title'), max_length=100, blank=True)
    text = models.TextField(_('text'), blank=True)
    button = models.CharField(_('button'), help_text=_('label'), max_length=30, blank=True)
    url = models.CharField(_('URL'), help_text='CTA', max_length=100, blank=True)
    # background = models.CharField(_('background'), max_length=100, help_text=_('URL to image'))
    background = models.ImageField(_('background'), blank=True, null=True, default=None, upload_to='slides')
    # TODO: i18n

    class Meta:
        verbose_name = _(u'slide')
        verbose_name_plural = _(u'slides')
        ordering = ('position', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "#"
