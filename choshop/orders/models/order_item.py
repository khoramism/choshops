from django.db import models 
from .order import Order 
from shop.models import Product

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')

    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)


    def get_cost(self):
        return self.price * self.quantity
