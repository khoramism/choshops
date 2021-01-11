from django.contrib import admin
#from django.contrib.gis.admin import OSMGeoAdmin
from django.utils.html import format_html
from .models import Shop, Product, ProductTag, ProductSubTag
# Register your models here.
admin.site.register(Shop)
#admin.site.register(Product)
#admin.site.register(Category)
#admin.site.register(SubCategory)
#admin.site.register(Location)

@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ProductSubTag)
class ProductSubTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'cat']
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price')
    list_filter = ('active', 'date_updated')
    #list_editable = ('in_stock', )
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Product, ProductAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_tag', 'product_name')
    readonly_fields = ('thumbnail',)
    search_fields = ('product__name',)
    def thumbnail_tag(self, obj):
        if obj.thumbnail:
            return format_html(
                '<img src="%s"/>' % obj.thumbnail.url
            )
        return "-"
    thumbnail_tag.short_description = "Thumbnail"
    def product_name(self, obj):
        return obj.product.name
#@admin.register(Location)
#class LocationAdmin(OSMGeoAdmin):
#   list_display = ['loc',]