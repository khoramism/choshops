from django.db import models
from django.urls import reverse
from core.shared import Postable
from .product import Product 
from .product_tag import ProductTag
from shop.managers import ProductCategoryManager

class ProductSubTag(Postable):
	
	name = models.CharField(max_length=50,verbose_name='نام زیر تگ')

	cat = models.ForeignKey(ProductTag, on_delete=models.CASCADE,verbose_name='نام تگ اصلی ')

	products = models.ManyToManyField(Product, blank=True) 
	
	objects = ProductCategoryManager()

	def __str__(self):
		return f'{self.name} in {self.cat}' 

	class Meta:
		ordering = ('name', )
		verbose_name ='زیرتگ '
		verbose_name_plural = 'زیرتگ ها '
