"""choshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.views.decorators.csrf import csrf_protect, csrf_exempt
from graphene_django.views import GraphQLView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    # added 
    path('account/', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('shop.urls')),
    path('orders', include('orders.urls')),
    path('markers', include('markers.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
