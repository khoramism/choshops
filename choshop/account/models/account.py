from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone 
from django.urls import reverse, reverse_lazy

class AccountManager(BaseUserManager):
	use_in_migrations = True 

	def _create_user(self, email, username, phone,password, **extra_fields):
		values = [email,username, phone]
		field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
		for field_name, value in field_value_map.items():
			if not value: 
				raise ValueError(f'the {field_name} value must be set!')


		email = self.normalize_email(email)
		
		user = self.model(email=email, username=username, phone=phone, **extra_fields)

		user.set_password(password)

		user.save(using=self._db)

		return user 

	def create_user(self, email,username,phone,password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, username, phone,password, **extra_fields)

	
	def create_staff(self, email, username, phone, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, username, phone,password, **extra_fields)


	def create_superuser(self, email, username, phone, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		return self._create_user(email, username, phone,password, **extra_fields)

class Account(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=40, unique=True)
	phone = models.CharField(max_length=50)
	bio = models.CharField(max_length=140, blank=True, default='')
	# date_of_birth = models.DateField(blank=True, null=True)
	avatar = models.ImageField(blank=True, null=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(default=timezone.now)
	last_login = models.DateTimeField(null=True)
	# Do apply this with IP as well 
	address = models.CharField(max_length=250)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	postal_code = models.CharField(max_length=20)
	city = models.CharField(max_length=100)
	
	objects = AccountManager()
	# USERNAME_FIELD is the name of the field on the user model that is used as the unique identifier.
	USERNAME_FIELD = 'email'
	# REQUIRED_FIELDS are the mandatory fields other than the unique identifier
	REQUIRED_FIELDS = ['username', 'phone']


# https://dev.to/joshwizzy/customizing-django-authentication-using-abstractbaseuser-llg
	class Meta:
		unique_together = ('email', 'username', 'phone')

	def __str__(self):
		return f'@{self.username}'

	def get_short_name(self):
		return self.username

	def get_absolute_url(self):
		return reverse("account:profile_detail", kwargs={"pk": self.pk})	
	#class Meta:
	#	abstract = True 
	
