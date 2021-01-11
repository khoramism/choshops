from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
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

	
class ActiveManager(models.Manager):
    def active(self):
        return self.filter(active=True)	
	

class Postable(TimeStampedModel):
	active = models.BooleanField(default=True)
	
	slug = models.SlugField(max_length=100, verbose_name='لینک',default='')

	summary = models.CharField(max_length=300,blank=True,null=True,verbose_name='خلاصه')

	objects = ActiveManager()

	# Model_Name.objects.active() 
	 
	# Is now defind in all Models Across the whole application 
	
	class Meta:
		abstract = True


class MetaTagsBase(models.Model):
	"""
	Abstract base class for generating meta tags
	"""
	meta_keywords = models.CharField(
		_("Keywords"),
		max_length=255,
		blank=True,
		help_text=_("Separate keywords with commas."),
	)
	meta_description = models.CharField(
		_("Description"),
		max_length=255,
		blank=True,
	)
	meta_author = models.CharField(
		_("Author"),
		max_length=255,
		blank=True,
	)
	meta_copyright = models.CharField(
		_("Copyright"),
		max_length=255,
		blank=True,
	)
	class Meta:
		abstract = True
	def get_meta_field(self, name, content):
		tag = ""
		if name and content:
			tag = render_to_string("core/includes/meta_field.html",
			{
			"name": name,
			"content": content,
			})
		return mark_safe(tag)
	
	def get_meta_keywords(self):
		return self.get_meta_field("keywords", self.meta_keywords)
	
	def get_meta_description(self):
		return self.get_meta_field("description", self.meta_description)
	
	def get_meta_author(self):
		return self.get_meta_field("author", self.meta_author)
	
	def get_meta_copyright(self):
		return self.get_meta_field("copyright",self.meta_copyright)
	def get_meta_tags(self):
		return mark_safe("\n".join((self.get_meta_keywords(),
			self.get_meta_description(),
			self.get_meta_author(),
			self.get_meta_copyright(),
			)))

'''
Once you have a method to run on a signal emission, the method must be decorated with the
@receiver annotation, which generally uses two arguments: a signal to listen for – those described in
Table 7-5 – which is a required argument and the optional sender argument to specify which model class to
listen into for the signal. If you want to listen for the same signal emitted by all your project’s models – a rare
case – you can omit the sender argument.
'''

