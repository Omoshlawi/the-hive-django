from django.db.models import Q
from django_filters import FilterSet, NumberFilter, CharFilter

from agents.models import Agent
from properties.models import Property
from django.utils import timezone


class AgentFilterSet(FilterSet):
    class Meta:
        model = Agent
        fields = ()
