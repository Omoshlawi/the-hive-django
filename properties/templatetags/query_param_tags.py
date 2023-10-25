from django import template

register = template.Library()


@register.simple_tag
def add_query_param(request, param_name, param_value):
    query_dict = request.GET.copy()
    query_dict[param_name] = param_value
    return f'?{query_dict.urlencode()}'
