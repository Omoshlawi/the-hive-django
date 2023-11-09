from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
]
