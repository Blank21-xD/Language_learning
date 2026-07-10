from django.shortcuts import render, redirect
from django.db import connection
from .models import Category, Vocabulary, UserProfilereview, GuestbookEntry, SecurityIncidentLog
import sys


def home(request):
    return render(request, 'korean_app/home.html')


def greetings(request):
    # This queries the database to get all entries in the Vocabulary table
    all_words = Vocabulary.objects.all()

    context = {
        'vocabulary_list': all_words
    }
    return render(request, 'korean_app/greetings.html', context)


def slang(request):
    # This filters the database to show only entries where the category name is 'Slang'
    slang_words = Vocabulary.objects.filter(category__name='Slang')

    context = {
        'vocabulary_list': slang_words
    }
    return render(request, 'korean_app/slang.html', context)


def guestbook(request):
    security_error = None

    if request.method == "POST":
        comment = request.POST.get('comment')
        # Simple security check: if it contains scripts or suspicious tags
        if "<script>" in comment.lower():
            security_error = "Malicious input detected and blocked."
            # Log the incident
            SecurityIncidentLog.objects.create(
                attacker_ip=request.META.get('REMOTE_ADDR'),
                flagged_comment=comment
            )
        else:
            GuestbookEntry.objects.create(username="Learner", comment=comment)

    entries = GuestbookEntry.objects.all().order_by('-timestamp')
    return render(request, 'korean_app/guestbook.html', {'entries': entries, 'security_error': security_error})
