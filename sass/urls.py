from django.urls import path
from . import views

app_name = 'sass'

urlpatterns = [
    path("", views.index, name='pricing-list')
]