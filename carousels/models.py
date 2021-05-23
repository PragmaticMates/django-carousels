from django.db import models
from django.utils.translation import ugettext_lazy as _, pgettext_lazy


class Carousel(models.Model):
    slug = models.SlugField(verbose_name=_('identifier'), help_text=_('slug'), unique=True, max_length=20)
    # TODO: settings (controls, speed, ...)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = _('carousel')
        verbose_name_plural = _('carousels')


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
