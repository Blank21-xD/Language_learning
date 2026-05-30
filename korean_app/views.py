from django.shortcuts import render
from django.db import connection
from .models import Category, Vocabulary, UserProfilereview, GuestBookComment


def home(request):
    return render(request, 'korean_app/home.html')


def greetings(request):
    return render(request, 'korean_app/greetings.html')


def slang(request):
    return render(request, 'korean_app/slang.html')


def guestbook(request):
    context = {
        'is_attack': False,
    }
    return render(request, 'korean_app/guestbook.html', context)
