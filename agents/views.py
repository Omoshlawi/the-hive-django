from django.shortcuts import render

from agents.filters import AgentFilterSet
from agents.models import Agent
from core.view_x import ViewX


# Create your views here.

class AgentsView(ViewX):
    template_path = "properties/index.html"
    filterset_class = AgentFilterSet
    queryset = Agent.published_objects.all()
    object_lookup = 'agent'
    list_template = 'agents/agents.html'
    detail_template = "agents/agent-page.html"


