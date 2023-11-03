from django_filters import FilterSet, NumberFilter, CharFilter

from properties.models import Property


class PropertyFilterSet(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr='gte', label="Minimum Price")
    max_price = NumberFilter(field_name="price", lookup_expr='lte', label="Maximum Price")
    category = CharFilter(method='filter_category')

    def filter_category(self, queryset, name, value):
        return queryset.filter(**{'type__name__in': [value]})

    class Meta:
        model = Property
        fields = ('name',)
