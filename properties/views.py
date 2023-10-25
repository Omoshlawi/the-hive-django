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

    def get(self, request):
        display_mode = request.GET.get('display_mode', 'list')
        filtered = self.filter_objects(request, queryset=self.get_queryset())
        properties = self.paginate_objects(request, filtered)
        context = {
            'properties': properties,
            'display_mode': display_mode
        }
        # print(context)
        return render(request, self.template_path, context)


