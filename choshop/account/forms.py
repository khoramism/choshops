from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Account 

class RegisterationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	
	class Meta:
		
		model = Account
		fields = ('email', 'name', 'phone', 'date_of_birth', 'picture', 'password')
	def save(self, commit=True):
		# Save the provided passsword in hashed format 
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user


class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password taiied', widget=forms.PasswordInput)

	class Meta: 
		model = Account
		fields =  ('email', 'name', 'phone', 'date_of_birth', 'picture', 'is_staff', 'is_superuser')

	def clean_password2(self):
		# Check that the Two password entries Match!?
		password1 = self.cleaned_data.get("password1"), 
		password2 = self.cleaned_data.get("password2")

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('PassWord ha yeki nistan dwsh !')
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
		fields = ('email', 'name', 'phone', 'date_of_birth', 'picture', 'password', 'is_active', 'is_superuser')

	def clean_password(self):
		# regardless of what the user provides, return the initial Value.
		# This is done here, rather than on the field, because the feild does not have access to the initial value 
		return self.initial['password']

	


















