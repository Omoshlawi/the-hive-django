from django.urls import path
from . import views

app_name = "agencies"

urlpatterns = [
    path("", views.index, name='agency-list')
]
