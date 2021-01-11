from django.shortcuts import render, reverse_lazy
from 
# Create your views here.
import json

from .models import Marker, Address
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize
from django.views import generic


class MarkersMapView(generic.base.TemplateView):
	"""Markers map view."""

	template_name = "map.html"

	def get_context_data(self, **kwargs):
		"""Return the view context data."""
		context = super().get_context_data(**kwargs)
		context["markers"] = json.loads(serialize("geojson", Marker.objects.all()))
		return context

class AddressListView(LoginRequiredMixin, generic.ListView):
	model = Address
	template_name = 'address/address_list.html'

	def def get_queryset(self):
		return self.model.objects.filter(account=self.request.user)

class AddressCreateView(LoginRequiredMixin, generic.edit.CreateView):
	model = Address
	fields = [
		'name',
		'address1',
		'address2',
		'zip_code',
		'city', 
		'country'
	]
	success_url = reverse_lazy('address_list')
	template_name = 'address/address_form.html'

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.account = self.request.user
		obj.save()
		return super().form_valid(form)

class AddressUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
	model = Address
	fields = [
		'name',
		'address1',
		'address2',
		'zip_code',
		'city', 
		'country'
	]
	template_name = 'address/address_update.html'

	success_url = reverse_lazy('address_list')
	
	def def get_queryset(self):
		return self.model.objects.filter(account=self.request.user)


class AddressDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
	model = models.Address
    success_url = reverse_lazy("address_list")
	template_name = 'address/address_confirm_delete'
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)