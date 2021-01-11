from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm,ReadOnlyPasswordHashField
from .models import Account 

class RegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	
	class Meta:
		
		model = Account
		fields = ('email', 'username', 'phone', 'avatar', 'password')
	def save(self, commit=True):
		# Save the provided passsword in hashed format 
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user


class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label='پسورد', widget=forms.PasswordInput)
	password2 = forms.CharField(label='تایید پسورد', widget=forms.PasswordInput)

	class Meta: 
		model = Account
		fields =  ('email', 'username', 'phone', 'avatar')

	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['email'].label = 'آدرس ایمیل شما' 
		self.fields['phone'].label = 'شماره همراه شما' 
		self.fields['username'].label = 'نام کاربری شما' 
		self.fields['picture'].label = 'آواتار شما' 
	
	def clean_password2(self):
		# Check that the Two password entries Match!?
		password1 = self.cleaned_data.get("password1"), 
		password2 = self.cleaned_data.get("password2")

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('رمز عبور های شما یکی نیستند جناب !!')
		return password2 

	def save(self, commit=True):
		# Save the provided password in hashed format 
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()

		return user 


class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = Account
		fields = ('email', 'username', 'phone', 'avatar', 'password')

	def clean_password(self):
		# regardless of what the user provides, return the initial Value.
		# This is done here, rather than on the field, because the feild does not have access to the initial value 
		return self.initial['password']

	'''

class LoginForm(AuthenticationForm):
	email = forms.EmailField(widget=forms.EmailInput())
	password = forms.CharField(label='پسورد', widget=forms.PasswordInput)
	class Meta:
		model = Account
		fields = ('email', 'password')
	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['email'].label = 'آدرس ایمیل شما' 



'''











