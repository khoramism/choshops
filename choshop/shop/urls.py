from . import views 
from django.urls import path,include

app_name = 'shop'

urlpatterns = [
   path('product_detail/<int:id>/<slug:slug>',views.product_list, name='product_detail'),
   path('product_list/',views.product_detail, name='product_list'),

]
