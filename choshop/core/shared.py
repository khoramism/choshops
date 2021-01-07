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
	publish = models.DateTimeField(default = timezone.now, verbose_name='انتشار')
	
	updated = models.DateTimeField(auto_now = True,verbose_name='آپدیت')
	
	class Meta:
		abstract = True


class Postable(TimeStampedModel):
	#is_active = models.BooleanField(default=True)
	
	meta_keywords = models.CharField(max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')

	meta_description = models.CharField(max_length=255, help_text='Content for description meta tag')

	slug = models.SlugField(max_length=100, verbose_name='لینک',default='')

	summary = models.CharField(max_length=300,blank=True,null=True,default='')

	image = models.ImageField(verbose_name='تصویر', upload_to='media/')

	class Meta:
		abstract = True