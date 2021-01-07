from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart 
from .forms import CartAddProductForm
from shop.models import Product 
# Create your views here.
# You use the require_POST decorator to allow only POST requests
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST) 
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])

    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

'''
You create an instance of CartAddProductForm for each item in the cart to allow
changing product quantities. You initialize the form with the current item quantity
and set the override field to True so that when you submit the form to the cart_
add view, the current quantity is replaced with the new one.
'''

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True,
        })
    return render(request, 'cart/detail.html', {'cart':cart})

