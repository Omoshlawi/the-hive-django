from django_filters import FilterSet, NumberFilter

from properties.models import Property


class PropertyFilterSet(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr='gte', label="Minimum Price")
    max_price = NumberFilter(field_name="price", lookup_expr='lte', label="Maximum Price")
    class Meta:
        model = Property
        fields = ('name',)

