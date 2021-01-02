from django.contrib import admin
from .models import Shop, Product, Category, SubCategory, Location 
# Register your models here.
admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Location)