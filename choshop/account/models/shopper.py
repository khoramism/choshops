# Django Imports 
from django.db import models
from django.utils import timezone 
from django.urls import reverse, reverse_lazy
# project Imports 
from shop.models import Shop 
from .account import Account 

class Shopper(Account):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)