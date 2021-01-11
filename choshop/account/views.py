from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout 
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, DetailView, TemplateView, View
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic 
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
# Our Project 
from .models import Account
from .forms import RegistrationForm, UserCreationForm


class RegistrationView(CreateView):
	template_name = 'registration/register.html'
	#form_class = RegistrationForm
	form_class = UserCreationForm
	def get_context_data(self, *args, **kwargs):
		context = super(RegistrationView, self).get_context_data(*args, **kwargs)
		context['next'] = self.request.GET.get('next')
		return context

	def get_success_url(self):
		next_url = self.request.POST.get('next')
		success_url = reverse('login')
		if next_url:
			success_url += '?next={}'.format(next_url)

		return success_url

class ProfileView(UpdateView):
	model = Account
	fields = ['username', 'phone', 'date_of_birth', 'picture']
	template_name = 'registration/profile.html'

	def get_success_url(self):
		return reverse('index')

	def get_object(self):
		return self.request.user

class LogoutView(generic.RedirectView):
	url = reverse_lazy('home')

	def get(self, request, *args, **kwargs):
		logout(request)
		return super().get(request, *args, **kwargs)
'''

class LoginView(generic.FormView):
	form_class = LoginForm
	success_url = reverse_lazy('shop:list')
	template_name = 'registeration/login.html'

	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		
		return form_class(self.request, **self.get_form_kwargs())

	def form_valid(self, form):
		auth_login(self.request, form.get_user())
		return super().form_valid(form)
'''
### TRAININGS 
from . import mixins 
class HomeView(TemplateView):
	template_name = 'registration/home.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['fake_num'] = 8 
		return context


class AccountListView(CreateView,ListView):
	model = Account
	context_object_name = 'accounts'
	fields = ('username', 'email')
	template_name = 'account/registeration/account_list.html'
	
class AccountDetailView(DetailView, UpdateView):
	model = Account
	fields = ('username', 'email')
	template_name = 'account/registeration/account_detail.html'

	#def 
class AccountCreateView(LoginRequiredMixin,mixins.PageTitleMixin,CreateView):
	model = Account
	fields = ('username', 'email', 'password')
	page_title = 'Create'

	
	def get_initial(self):
		initial = super().get_initial()
		initial['username'] = self.request.user.username 
		return initial
	 
class AccountUpdateView(LoginRequiredMixin,mixins.PageTitleMixin,UpdateView):
	fields = ('username', 'email')
	model = Account
	def get_page_title(self):
		obj = self.get_object()
		return f"Update {obj.username}"



class AccountDeleteView(LoginRequiredMixin,DeleteView):
	model = Account
	success_url = reverse_lazy('account:list_account')

	def get_queryset(self):
		if self.request.user.is_staff:
			return self.model.objects.filter(username='alireza')
		return self.model.objects.all() 