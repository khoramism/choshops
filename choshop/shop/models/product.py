from django.db import models
from django.conf import settings 
#from django.contrib.gis.db import models as gis_models 
from account.models import Account 
from .tag_product import ProductTag 
from .product_image import ProductImage
from .product_sub_tag import ProductSubTag 
from core.shared import Postable
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
# Storage 

from .storages import ProtectedStorage


from .shop import Shop


def get_storage_location():
	if settings.DEBUG:
		return ProtectedStorage()

class Product(Postable): 
	#STATUS_CHOICES = (
	#	('available', "موجود"),
	#	('out', 'ناموجود')
	#)
	name = models.CharField(default='ghups', max_length=50,verbose_name='نام محصول ')
	
	description = RichTextUploadingField(verbose_name='توضیحات')
	
	available = models.BooleanField(default=True,verbose_name='موجوده')
	
	numbers = models.PositiveSmallIntegerField(verbose_name='تعداد محصول')

	is_finishing = models.BooleanField(verbose_name='آیا محصول در آستانه به پایان رسیدن است؟', default=False)

	tags = models.ManyToManyField(ProductTag,verbose_name='تگ')	

	sub_tags = models.ManyToManyField(ProductSubTag,verbose_name='زیر تگ')

	for_the_shop = models.ForeignKey(Shop, on_delete=models.CASCADE,verbose_name='برای فروشگاهه')

	price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='قیمت')
	
	image = models.ForeignKey(ProductImage, on_delete=True)

	video_link = models.URLField(blank=True, null=True ,verbose_name='لینک ویدیو')
	
	media = models.FileField(storage=ProtectedStorage, upload_to='products/', null=True, blank=True,verbose_name='فایل غیره')
	
	is_bestseller = models.BooleanField(default=False,verbose_name='بهترین فروش رو داشته؟')
	
	old_price = models.DecimalField(max_digits=9,decimal_places=2, blank=True,default=0.00,verbose_name='قیمت قدیمی')
	
	sku = models.CharField(max_length=50 ,verbose_name='شناسه اصلی ')
	
	requires_shipping = models.BooleanField(default=False,verbose_name='آیا نیاز به جابجایی داره؟')
		
	can_backorder = models.BooleanField(default=False,verbose_name='آیا پس گرفته میشه؟')
	
	@property
	def can_order(self):
		if self.has_inventory():
			return True
		elif self.can_backorder:
			return True
		return False
	
	@property
	def order_btn_title(self):
		if self.can_order and not self.has_inventory():
			return "Backorder"
		if not self.can_order:
			return "Cannot purchase."
		return "Purchase"

	def has_inventory(self):
		return self.numbers > 0 # True or False

	def remove_items_from_inventory(self, count=1, save=True):
		current_inv = self.numbers
		current_inv -= count
		self.numbers = current_inv
		if save == True:
			self.save()
		return self.numbers	

