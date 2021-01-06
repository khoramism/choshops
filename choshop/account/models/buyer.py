from django.db import models
from django.utils import timezone 
from django.urls import reverse, reverse_lazy
from shop.models import Shop 
from .account import Account 


class Buyer(Account):
    pass
		#permissions = (
	#		('ban_member', 'can ban member')
		#)
