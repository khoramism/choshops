from django.db import models 
from .product import Product



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    image = models.ImageField(upload_type='product-images')

    thumbnail = models.ImageField(upload_to='product-thumbnails', null=True)

    