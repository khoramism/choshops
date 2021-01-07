from django.db import models
#from django.contrib.gis.db import models as gis_models 
#from account.models import Account 

from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
# class Shop 
# class Issiues 
# class Images 
# class Products Done 
# class Session(CARD or Sth like that) Done 

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

