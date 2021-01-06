from django.db import models
from django.urls import reverse
from .shared import Postable
from .category import Category

class SubCategory(Postable):
	
	name = models.CharField(max_length=50)

	cat = models.ForeignKey(Category, on_delete=models.CASCADE)


	def __str__(self):
		return f'{self.name} in {self.cat}' 

	class Meta:
		ordering = ('name', )
		verbose_name ='زیرتگ '
		verbose_name_plural = 'زیرتگ ها '
