from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from account.models import Account 
# Create your models here.

def dir_path(instance, filename): 

	# file will be uploaded to MEDIA_ROOT / auth /user_<id>/<filename>

	if instance.__class__.__name__ == 'Language':

		return f'media/uploads/images/{instance.__class__.__name__}/{instance.name}/{filename}'

	elif instance.__class__.__name__ == "Intro":

		return f'media/uploads/images/Language/{instance.__class__.__name__}/{instance.name}/{filename}'

class Post(models.Model):

	STATUS_CHOICES = (
		('draft', 'در حال انتظار'),
		('published', 'منتشر شده'),
		)

	title = models.CharField(max_length=100,default='')

	summary = models.CharField(max_length=300,blank=True,null=True,default='')

	description = RichTextUploadingField()
	
	#cat = TaggableManager()
	
	publish = models.DateTimeField(default = timezone.now, verbose_name='انتشار')
	
	created = models.DateTimeField(auto_now_add = True, verbose_name='ساخت',null=True)
	
	updated = models.DateTimeField(auto_now = True,verbose_name='آپدیت')
	
	status = models.CharField(max_length=60, choices = STATUS_CHOICES, default='draft', verbose_name='وضعیت')

	author = models.ForeignKey(Account,on_delete= models.SET_NULL,blank=True, null=True)
	
	#slug = models.SlugField(max_length=100, verbose_name='لینک',default='')

	def get_absolute_url(self):

		return reverse("blog:post_detail", args =[self.slug])

	# FIX THIS SLUGIFY PROBLEM 
	#def save(self):
	#	self.slug = slugify(self.title)
	#	super(Post,self).save()

