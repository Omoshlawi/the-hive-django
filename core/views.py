from django.shortcuts import render

from properties.models import PropertyType, Property, PropertyUnit


# Create your views here.
def index(request):
    property_types = PropertyType.objects.filter()
    property_units = PropertyUnit.objects.filter(published=True)
    conntext = {
        'property_types': property_types,
        'properties': property_units,

    }
    return render(request=request, template_name="core/home-5.html", context=conntext)


def pricing(request):
    return render(request, 'core/pricing.html')


def contact(request):
    return render(request, "core/contact.html")


def team(request):
    render(request, "core/team.html")