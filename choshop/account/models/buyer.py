from django.db import models
from django.utils import timezone 
from django.urls import reverse, reverse_lazy
from shop.models import Shop 
from .account import Account

class Buyer(models.Model):
    account = models.OneToOneField(Account)
	#shop = models.
	
	
		#permissions = (
	#		('ban_member', 'can ban member')
		#)
