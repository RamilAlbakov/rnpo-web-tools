"""network_live app url configuration."""

from django.urls import path

from .views import network_live

urlpatterns = [
    path('', network_live, name='network_live'),
]
