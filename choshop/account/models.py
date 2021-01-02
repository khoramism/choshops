from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone 
from shop.models import Shop 





class AccountManager(BaseUserManager):
	use_in_migrations = True 

	def _create_user(self, email, name, phone,password, **extra_fields):
		values = [email, name,  phone]
		field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
		for field_name, value in field_value_map.items():
			if not value: 
				raise ValueError(f'the {field_name} value must be set!')


		email = self.normalize_email(email)
		
		user = self.model(email=email, name=name, phone=phone, **extra_fields)

		user.set_password(password)

		user.save(using=self._db)

		return user 

	def create_user(self, email,name,phone,password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, name, phone,password, **extra_fields)

	
	def create_staff(self, email, name, phone, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, name, phone,password, **extra_fields)


	def create_superuser(self, email, name, phone, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		return self._create_user(email, name, phone,password, **extra_fields)

class Account(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	date_of_birth = models.DateField(blank=True, null=True)
	picture = models.ImageField(blank=True, null=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(default=timezone.now)
	last_login = models.DateTimeField(null=True)
	
	objects = AccountManager()
	# USERNAME_FIELD is the name of the field on the user model that is used as the unique identifier.
	USERNAME_FIELD = 'email'
	# REQUIRED_FIELDS are the mandatory fields other than the unique identifier
	REQUIRED_FIELDS = ['name', 'phone']


# https://dev.to/joshwizzy/customizing-django-authentication-using-abstractbaseuser-llg

	def get_full_name(self):
		return self.name

	def get_short_name(self):
		return self.name.split()[0]


	#class Meta:
	#	abstract = True 


class Buyer(Account):
	pass


class Shopper(Account):
	shops = models.OneToOneField(Shop, on_delete=models.CASCADE)

	






















