from . import views 
from django.urls import path,include

app_name = 'shop'

urlpatterns = [
   path('product_detail/<int:id>/<slug:slug>',views.product_list, name='product_detail'),
   path('product_list/',views.product_detail, name='product_list'),
   path(
        "products/<slug:tag>/",
        views.ProductListView.as_view(),
        name="products",
    ),
    path('product/<slug:slug>', views.ProductDetailview.as_view(), name='product')
]
