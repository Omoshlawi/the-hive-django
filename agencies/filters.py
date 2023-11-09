from django_filters import FilterSet

from agencies.models import Agency


class AgencyFilterSet(FilterSet):
    class Meta:
        model = Agency
        fields = ('name',)
