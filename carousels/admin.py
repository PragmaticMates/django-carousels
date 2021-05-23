from django.contrib import admin

from carousels.models import Carousel, Slide


class SlideInline(admin.StackedInline):
    model = Slide
    extra = 3
    fields = ['position', 'title', 'text', 'button', 'url', 'background']


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    search_fields = ('slug',)
    list_display = ('id', 'slug')
    list_editable = ('slug',)
    inlines = [SlideInline]


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    search_fields = ('title', 'text', 'button', 'URL')
    list_display = ('id', 'title', 'carousel', 'button', 'url', 'background', 'position')
    list_display_links = ['id', 'title']
    # list_editable = ('title', 'button', 'url', 'position', 'background')
    list_filter = ['carousel']
