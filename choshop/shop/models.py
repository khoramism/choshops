from django.db import models
#from account.models import Account 

from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
# class Shop 
# class Issiues 
# class Images 
# class Products
# class Session(CARD or Sth like that) 
class Category(models.Model):
	pass

class SubCategory(models.Model):
	pass

class Location(models.Model):
	pass

class Shop(models.Model):
	name = models.CharField(default= 'ChoShop', max_length=50)
	
	loc = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
	
	#shopper = models.OneToOneField(Shopper, on_delete=models.CASCADE)
	#products = models.ForeignKey(Product, )

	def __str__(self):
		return f'{self.name} with the ownership of {self.shpper.email}'


class Product(models.Model):
	STATUS_CHOICES = (
		('available', "موجود"),
		('out', 'ناموجود')
	)
	title = models.CharField(default='ghups', max_length=50)
	
	summary = models.CharField(max_length=200)
   
	description = RichTextUploadingField()
	
	publish = models.DateTimeField(default = timezone.now, verbose_name='انتشار')
	
	created = models.DateTimeField(auto_now_add = True, verbose_name='ساخت',null=True)
	
	updated = models.DateTimeField(auto_now = True,verbose_name='آپدیت')
	
	status = models.CharField(max_length=60, choices = STATUS_CHOICES, default='draft', verbose_name='وضعیت')

	numbers = models.PositiveSmallIntegerField()

	is_finishing = models.BooleanField(verbose_name='آیا محصول در آستانه به پایان رسیدن است؟', default=False)

	category = models.ManyToManyField(Category)	

	sub_category = models.ManyToManyField(SubCategory)	

	for_the_shop = models.ForeignKey(Shop, on_delete=models.CASCADE)



	def save(self):
		# SUper ... 
		if self.numbers > 15:
			self.is_finishing = False 

		if self.numbers <= 15:
			self.is_finishing = True  