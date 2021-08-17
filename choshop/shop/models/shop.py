from django.db import models
#from django.contrib.gis.db import models as gis_models 
from account.models import Account
from .tag_product import ProductTag 
from .product_sub_tag import ProductSubTag 
#from .product import Product
from core.shared import Postable
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Shop(models.Model):
	name = models.CharField(default= 'ChoShop', max_length=50, verbose_name='نام فروشگاه')
	
	#loc = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
	
	#shopper = models.OneToOneField(Shopper, on_delete=models.CASCADE)
	
	#products = models.ForeignKey(Product,on_delete=models.CASCADE )

	def __str__(self):
		return f'{self.name} with the ownership of {self.shpper.email}'


