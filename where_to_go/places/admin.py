from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview']
    
    def get_preview(self, obj):
        if obj.image:
            return mark_safe(f"<img src ='{obj.image.url}' width='100' height='100'>")
        else:
            return '-'


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin,admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('number','get_photo')
    readonly_fields = ('get_photo',)

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f"<img src ='{obj.image.url}' width='70'>")
        else:
            return '-'


# Register your models here.
