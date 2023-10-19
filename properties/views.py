from django.shortcuts import render

from properties.models import PropertyUnit


# Create your views here.


def properties(request):
    display_mode = request.GET.get('display_mode', 'list')
    context = {
        'properties': PropertyUnit.objects.filter(published=True),
        'display_mode': display_mode
    }
    print(context)
    return render(request, "properties/index.html", context)
