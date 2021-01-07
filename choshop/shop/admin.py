from django.contrib import admin
#from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop, Product, Category, SubCategory 
# Register your models here.
admin.site.register(Shop)
#admin.site.register(Product)
#admin.site.register(Category)
#admin.site.register(SubCategory)
#admin.site.register(Location)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'cat']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'publish', 'updated']
    list_filter = ['publish', 'updated']
    list_editable = ['price',]
    prepopulated_fields = {'slug': ('name',)}


#@admin.register(Location)
#class LocationAdmin(OSMGeoAdmin):
#   list_display = ['loc',]