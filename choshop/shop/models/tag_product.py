from django.db import models
from django.urls import reverse
from core.shared import Postable
#from .product import Product

from shop.managers import ProductCategoryManager
'''
Django offers a special type of field called ManyToManyField, which
automatically creates a linking table between two tables, in this case Product
Tags and Products. This linking table allows you to create relationships
where any tags can be associated to any products and vice versa.
'''

class ProductTag(Postable):
	
	name = models.CharField(max_length=50,verbose_name='نام تگ')

	#products = models.ManyToManyField(Product, blank=True) 
	
	
	objects = ProductCategoryManager()

	def __str__(self):
		return self.name 

	def natural_key(self):
		return (self.slug,)
	
	class Meta:
		ordering = ('name', )
		verbose_name = 'تگ'
		verbose_name_plural = 'تگ ها '
