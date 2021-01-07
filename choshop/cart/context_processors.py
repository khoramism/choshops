from .cart import Cart 

def cart(request):
    return {'cart': Cart(request)}

'''

The cart context processor will be executed every time a template is rendered
using Django's RequestContext . The cart variable will be set in the context
of your templates. You can read more about RequestContext at https://
docs.djangoproject.com/en/3.0/ref/templates/api/#django.template.
RequestContext .

Context processors are executed in all the requests that use
RequestContext. You might want to create a custom template
tag instead of a context processor if your functionality is not
needed in all templates, especially if it involves database queries.
'''