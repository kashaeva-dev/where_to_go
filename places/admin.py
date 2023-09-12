from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from places.models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 200px;"/>', mark_safe(obj.image.url))


@admin.register(Place)
class PlaceAdmin( SortableAdminBase, admin.ModelAdmin):
    inlines = (ImageInline, )
    search_fields = ('title', )
