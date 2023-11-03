from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views import View

from core.view_x import ViewX
from properties.filters import PropertyFilterSet
from properties.models import PropertyUnit


# Create your views here.

class PropertyView(ViewX):
    template_path = "properties/index.html"
    filterset_class = PropertyFilterSet
    queryset = PropertyUnit.objects.filter(published=True)
    object_lookup = 'property'
    list_template = 'properties/index.html'
    detail_template = 'properties/single-property-1.html'

    def get_context(self, request) -> dict:
        display_mode = request.GET.get('display_mode', 'list')
        context = super().get_context(request)
        context.update({'display_mode': display_mode})
        return context
