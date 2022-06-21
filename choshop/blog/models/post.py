from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from account.models import Account 
from core.shared import Postable
from .sub_category import SubCategory
from .category import Category

class Post(models.Model):

	STATUS_CHOICES = (
		('draft', 'در حال انتظار'),
		('published', 'منتشر شده'),
		)

	title = models.CharField(max_length=100,default='')

	summary = models.CharField(max_length=300,blank=True,null=True,default='')

	description = RichTextUploadingField()
	
	cat = models.ForeignKey(Category, on_delete=models.CASCADE)
	
	sub_cat = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
	
	status = models.CharField(max_length=60, choices = STATUS_CHOICES, default='draft', verbose_name='وضعیت')

	author = models.ForeignKey(Account,on_delete= models.SET_NULL,blank=True, null=True)
	

	def get_absolute_url(self):

		return reverse("blog:post_detail", args =[self.slug])

	# FIX THIS SLUGIFY PROBLEM 
	#def save(self):
	#	self.slug = slugify(self.title)
	#	super(Post,self).save()