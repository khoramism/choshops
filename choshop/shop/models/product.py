from django.db import models
#from django.contrib.gis.db import models as gis_models 
from account.models import Account 
from .product_category import Category 
from .product_sub_category import SubCategory 
from core.shared import Postable
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from .shop import Shop


class Product(Postable): 
	#STATUS_CHOICES = (
	#	('available', "موجود"),
	#	('out', 'ناموجود')
	#)
	name = models.CharField(default='ghups', max_length=50)
	
	description = RichTextUploadingField()
	
	available = models.BooleanField(default=True)
	
	numbers = models.PositiveSmallIntegerField()

	is_finishing = models.BooleanField(verbose_name='آیا محصول در آستانه به پایان رسیدن است؟', default=False)

	category = models.ManyToManyField(Category)	

	sub_category = models.ManyToManyField(SubCategory)	

	for_the_shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

	price = models.DecimalField(max_digits=10, decimal_places=2)

	image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
	
	
	is_bestseller = models.BooleanField(default=False)
	
	is_featured = models.BooleanField(default=False)
	
	old_price = models.DecimalField(max_digits=9,decimal_places=2, blank=True,default=0.00)
	
	sku = models.CharField(max_length=50)
	
	def save(self):
		# SUper ... 
		if self.numbers > 15:
			self.is_finishing = False 

		if self.numbers <= 15:
			self.is_finishing = True  