from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import (UsernameField,
										UserCreationForm as DjangoUserCreationForm,
										AuthenticationForm,
										ReadOnlyPasswordHashField)
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

'''

GOOD EXAMPLE 

class Lead(models.Model):
    name = models.CharField(max_length=32)
class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('name', )
# Creating a form to add a lead.
>>> form = LeadForm()
# Create a form instance with POST data for a new lead
>>> form = LeadForm(request.POST)
# Creating a form to change an existing lead.
>>> lead = Lead.objects.get(pk=1)
>>> form = LeadForm(instance=lead)
# Create a form instance with POST data for an existing lead
>>> form = LeadForm(request.POST, instance=lead)
# Creates the lead entry in the database, or
# triggers an update if an instance was passed in.
>>> new_lead = form.save()

'''

class AuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        strip=False, widget=forms.PasswordInput
    )
    def __init__(self, request=None, *args, **kwargs):
		self.fields['email'].label = 'آدرس ایمیل شما' 
		self.fields['phone'].label = 'شماره همراه شما' 
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)
    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        if email is not None and password:
            self.user = authenticate(
                self.request, email=email, password=password
            )
            if self.user is None:
               raise forms.ValidationError(
                   "ایمیل یا رمز عبور شما صحیح نمی باشد!"
               )
            logger.info(
                "Authentication successful for email=%s", email
            )
        return self.cleaned_data

    def get_user(self):
        return self.user




class UserCreationForm2(DjangoUserCreationForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = Account
        fields = ("email",)
        field_classes = {"email": UsernameField}

    def send_mail(self):
        logger.info(
            "Sending signup email for email=%s",
            self.cleaned_data["email"],
        )
        message = f"{self.cleaned_data["email"]} به به "
        send_mail(
            "به چوشاب خوش اومدین!",
            message,
            "site@booktime.domain",
            [self.cleaned_data["email"]],
            fail_silently=True,
        )




