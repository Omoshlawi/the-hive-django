from django.shortcuts import render

from agencies.filters import AgencyFilterSet
from agencies.models import Agency
from core.view_x import ViewX


# Create your views here.

class Agencies(ViewX):
    template_path = "properties/index.html"
    filterset_class = AgencyFilterSet
    queryset = Agency.published_objects.all()
    object_lookup = 'agency'
    list_template = 'agencies/agencies.html'
    detail_template = 'agencies/agency-page.html'

