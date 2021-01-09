from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

"""

...
106 Django Design Patterns
and Best Practices

"""

class TimeStampedModel(models.Model):	
	created =models.DateTimeField(auto_now_add=True,verbose_name='ساخت')
	publish = models.DateTimeField(default = timezone.now,verbose_name='انتشار')
	updated = models.DateTimeField(auto_now = True,verbose_name='آپدیت')
	
	class Meta:
		abstract = True


class Postable(TimeStampedModel):
	#is_active = models.BooleanField(default=True)
	
	slug = models.SlugField(max_length=100, verbose_name='لینک',default='')

	summary = models.CharField(max_length=300,blank=True,null=True,verbose_name='خلاصه')

	class Meta:
		abstract = True