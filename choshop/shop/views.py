from django.shortcuts import render, get_object_or_404, redirect
from . import models 
# Create your views here.
from cart.forms import CartAddProductForm
from django.views import generic 



def product_detail(request, id, slug):
    product = get_object_or_404(models.Product, id=id, slug=slug, available=True)

    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product':product, 'cart_product_form':cart_product_form})


def product_list(request):
    return render(request, 'shop/product/list.html', {'products':models.Product.objects.all()})

class ProductListView(generic.ListView):
    template_name = 'shop/product/class-list.html'
    paginate_by = 4
    
    def get_queryset(self):
        tag = self.kwargs['tag']
        self.tag = None 
        if tag != 'all':
            self.tag = get_object_or_404(models.ProductTag, slug=tag)
        
        if self.tag:
            products = models.Product.objects.active().filter(tags=self.tag)
        
        else:
            products = models.Product.objects.active()
        return products.order_by("name")
'''
'Another thing worth mentioning in the template is how related models
are traversed. If a model has a foreign key to another table, it is possible to
call the methods of the related managers by just specifying their names.
object.tags.all in templates, for example, is equivalent to object.tags.
all() in Python.'''


class ProductDetailview(generic.DetailView):
    model = models.Product
    template_name = 'shop/product/class-detail.html'