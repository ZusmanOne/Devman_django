from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin
from django.utils.html import format_html


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    extra = 0
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        return format_html("<img src ='{}' width={} height={}", mark_safe(obj.image.url), '100', '100')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]


@admin.register(PlaceImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('number', 'id', 'place',)
