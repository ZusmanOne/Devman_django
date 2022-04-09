from django.contrib import admin
from .models import *


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInline]


admin.site.register(Image)
# Register your models here.
