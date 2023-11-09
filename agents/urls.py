from django.urls import path
from . import views

app_name = "agents"

urlpatterns = [
    path("", views.AgentsView.as_view(), name="agent-list"),
    path("<int:id>/", views.AgentsView.as_view(), name="agent-detail")
]
