from django.db import models
#from django.contrib.gis.db import models as gis_models 
#from account.models import Account 

from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
# class Shop 
# class Issiues 
# class Images 
# class Products
# class Session(CARD or Sth like that) 
class Category(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=20)
	description = models.TextField()
	is_active = models.BooleanField(default=True)
	
	meta_keywords = models.CharField(max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')

	meta_description = models.CharField(max_length=255, help_text='Content for description meta tag')

	created_at = models.DateTimeField(auto_now_add=True)

	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name 

	class Meta:
		ordering = ('name', )
		verbose_name = 'تگ'
		verbose_name_plural = 'تگ ها '

class SubCategory(models.Model):
	
	name = models.CharField(max_length=50)
	
	slug = models.SlugField(max_length=20)
	
	cat = models.ForeignKey(Category, on_delete=models.CASCADE)

	description = models.TextField()

	is_active = models.BooleanField(default=True)
	
	meta_keywords = models.CharField(max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')

	meta_description = models.CharField(max_length=255, help_text='Content for description meta tag')

	created_at = models.DateTimeField(auto_now_add=True)

	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.name} in {self.cat}' 

	class Meta:
		ordering = ('name', )
		verbose_name = 'تگ'
		verbose_name_plural = 'تگ ها '


class Location(models.Model):
	#loc = gis_models.PointField()
	pass

class Shop(models.Model):
	name = models.CharField(default= 'ChoShop', max_length=50)
	
	loc = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
	
	#shopper = models.OneToOneField(Shopper, on_delete=models.CASCADE)
	#products = models.ForeignKey(Product, )

	def __str__(self):
		return f'{self.name} with the ownership of {self.shpper.email}'


class Product(models.Model):
	#STATUS_CHOICES = (
	#	('available', "موجود"),
	#	('out', 'ناموجود')
	#)
	name = models.CharField(default='ghups', max_length=50)
	
	summary = models.CharField(max_length=200)
   
	description = RichTextUploadingField()
	
	publish = models.DateTimeField(default = timezone.now, verbose_name='انتشار')
	
	created = models.DateTimeField(auto_now_add = True, verbose_name='ساخت',null=True)
	
	updated = models.DateTimeField(auto_now = True,verbose_name='آپدیت')
	
	available = models.BooleanField(default=True)
	
	numbers = models.PositiveSmallIntegerField()

	is_finishing = models.BooleanField(verbose_name='آیا محصول در آستانه به پایان رسیدن است؟', default=False)

	category = models.ManyToManyField(Category)	

	sub_category = models.ManyToManyField(SubCategory)	

	for_the_shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

	price = models.DecimalField(max_digits=10, decimal_places=2)

	image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
	
	slug = models.SlugField(max_length=50)
	
	meta_keywords = models.CharField(max_length=255,help_text='Comma-delimited set of SEO keywords for meta tag')
	
	meta_description = models.CharField(max_length=255, help_text='Content for description meta tag')
	
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