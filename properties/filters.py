from django.db.models import Q
from django_filters import FilterSet, NumberFilter, CharFilter

from properties.models import Property
from django.utils import timezone


class PropertyFilterSet(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr='gte', label="Minimum Price")
    max_price = NumberFilter(field_name="price", lookup_expr='lte', label="Maximum Price")
    category = CharFilter(method='filter_category')
    status = CharFilter(field_name='status', lookup_expr='name__icontains')
    min_year = NumberFilter(field_name='property', lookup_expr='date_build__year__gte')
    max_year = NumberFilter(field_name='property', lookup_expr='date_build__year__lte')
    year = NumberFilter(field_name='property', lookup_expr='date_build__year')
    location = CharFilter(method='filter_location')

    def filter_location(self, qs, name, value):
        return qs.filter(
            Q(property__address__icontains=value) |
            Q(property__city__icontains=value) |
            Q(property__state__icontains=value)
        )

    def filter_category(self, queryset, name, value):
        return queryset.filter(**{'type__name__in': [value]})

    class Meta:
        model = Property
        fields = ('name', 'price')
