from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('greetings/', views.greetings, name="greetings"),
    path('slang/', views.slang, name="slang"),
    path('guestbook/', views.guestbook, name='guestbook'),

]
