from django.db import models
from account.models import Buyer 
# Create your models here.
class Order(models.Model):
    paid = models.BooleanField(default=False)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-created',)
   
    def __str__(self):
        return f'Order {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())



    