from django import template
from django.urls import reverse
from django.http import HttpRequest

register = template.Library()
import urllib3


@register.simple_tag
def add_query_param(request, param_name, param_value):
    query_dict = request.GET.copy()
    query_dict[param_name] = param_value
    return f'?{query_dict.urlencode()}'


@register.simple_tag
def is_active(request: HttpRequest, view_name):
    path = reverse(view_name)
    parsed_path = urllib3.util.parse_url(path)
    _is_active = "active" if request.path == parsed_path.path else None
    print(f"{_is_active=},{path=},{parsed_path.path=}")
    return _is_active
