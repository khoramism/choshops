# Create your models here.
#from django.contrib.gis.db.models import PointField
from django.db import models
from account.models import Account

class Marker(models.Model):
	"""A marker with name and location."""

	name = models.CharField(max_length=255)


class Address(models.Model):
	 SUPPORTED_COUNTRIES = (
		("ir", "ایران"),
		("us", "ایالات متحده آمریکا")
	)
	
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	name = models.CharField(max_length=60)
	address1 = models.CharField("Address line 1", max_length=60)
	address2 = models.CharField(
		"Address line 2", max_length=60, blank=True
	)
	zip_code = models.CharField(
		"ادرس پستی", max_length=12
	)
	city = models.CharField(max_length=60)
	country = models.CharField(
		max_length=3, choices=SUPPORTED_COUNTRIES
	)
	def __str__(self):
		return ", ".join(
			[
				 self.name,
				 self.address1,
				 self.address2,
				 self.zip_code,
				 self.city,
				 self.country,
			]
	   )