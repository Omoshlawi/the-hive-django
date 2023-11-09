from django.urls import path
from . import views

app_name = "agencies"

urlpatterns = [
    path("", views.Agencies.as_view(), name='agency-list'),
    path("<int:id>/", views.Agencies.as_view(), name='agency-detail')
]
