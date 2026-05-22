from django.urls import path
from .views import dictionary_search

urlpatterns = [
    path('', dictionary_search, name='dictionary_search'),
]
