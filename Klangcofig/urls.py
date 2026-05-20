from django.contrib import admin
from django.urls import path
from korean_app.views import dictionary_search

urlpatterns = [
    path('admin/', admin.site.urls),  #
    path('search/', dictionary_search,
         name='dictionary_search'),  # our playground url
]
