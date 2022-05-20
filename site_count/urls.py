from django.urls import path

from .views import count_sites, download_sites

urlpatterns = [
    path('', count_sites, name='count_site'),
    path('download/', download_sites, name='download_sites'),
]
