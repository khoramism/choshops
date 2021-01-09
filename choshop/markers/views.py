from django.shortcuts import render

# Create your views here.
import json

from .models import Marker

from django.core.serializers import serialize
from django.views.generic.base import TemplateView


class MarkersMapView(TemplateView):
	"""Markers map view."""

	template_name = "map.html"

	def get_context_data(self, **kwargs):
		"""Return the view context data."""
		context = super().get_context_data(**kwargs)
		context["markers"] = json.loads(serialize("geojson", Marker.objects.all()))
		return context