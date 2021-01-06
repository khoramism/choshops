from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from account.models import Account 

from django.utils import timezone
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
	
	cat = models.ForeignKey(Category)
	
	sub_cat = models.ForeignKey(SubCategory)
	
	status = models.CharField(max_length=60, choices = STATUS_CHOICES, default='draft', verbose_name='وضعیت')

	author = models.ForeignKey(Account,on_delete= models.SET_NULL,blank=True, null=True)
	

	def get_absolute_url(self):

		return reverse("blog:post_detail", args =[self.slug])

	# FIX THIS SLUGIFY PROBLEM 
	#def save(self):
	#	self.slug = slugify(self.title)
	#	super(Post,self).save()
"""
class TimeStampedModel(models.Model):
created = models.DateTimeField(auto_now_add=True)
modified = models.DateTimeField(auto_now =True)
class Meta:
abstract = True
class Postable(TimeStampedModel):
message = models.TextField(max_length=500)
...
class Meta:
abstract = True
class Post(Postable):
...
class Comment(Postable):
...
106 Django Design Patterns
and Best Practices

"""
# class Shop 
# class Issiues 
# class Images 
# class Products
# class Session(CARD or Sth like that) 
class Category(models.Model):
	
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name 

	class Meta:
		ordering = ('name', )
		verbose_name = 'تگ'
		verbose_name_plural = 'تگ ها '

class SubCategory(models.Model):
	
	name = models.CharField(max_length=50)

	cat = models.ForeignKey(Category, on_delete=models.CASCADE)


	def __str__(self):
		return f'{self.name} in {self.cat}' 

	class Meta:
		ordering = ('name', )
		verbose_name ='زیرتگ '
		verbose_name_plural = 'زیرتگ ها '
