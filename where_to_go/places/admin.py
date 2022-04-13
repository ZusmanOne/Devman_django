from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 0
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        return mark_safe(f"<img src ='{obj.image.url}' width='100' height='100'>")


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline,]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('number','id',)






# Register your models here.
