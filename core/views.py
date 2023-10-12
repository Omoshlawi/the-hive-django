from django.shortcuts import render

from properties.models import PropertyType


# Create your views here.
def index(request):
    property_types = PropertyType.objects.all()
    conntext = {
        'property_types': property_types
    }
    return render(request=request, template_name="core/home-5.html", context=conntext)
