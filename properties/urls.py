from django.urls import path
from . import views

app_name = "properties"
urlpatterns = [
    path("", views.PropertyView.as_view(), name='property-list'),
    path("<int:id>/", views.PropertyView.as_view(), name='property-detail')
]
