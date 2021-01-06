from django.db import models
from django.urls import reverse
from .shared import Postable



class Category(Postable):
	
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name 

	class Meta:
		ordering = ('name', )
		verbose_name = 'تگ'
		verbose_name_plural = 'تگ ها '
