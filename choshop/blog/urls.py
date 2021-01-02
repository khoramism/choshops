
from django.urls import path
from . import views 

urlpatterns = [
	path('detail',views.detail ,name='post_detail'),
	path('list',views.list_posts ,name='list_posts'),

]
