from django.shortcuts import render, redirect
from django.db import connection
from .models import Category, Vocabulary, UserProfilereview, GuestBookComment


def home(request):
    return render(request, 'korean_app/home.html')


def greetings(request):
    return render(request, 'korean_app/greetings.html')


def slang(request):
    return render(request, 'korean_app/slang.html')


def guestbook(request):
    is_attack = False

    # Check if the user is submitting the form
    if request.method == "POST":
        user_name = request.POST.get("username", "")
        user_comment = request.POST.get("comment", "")

        # Define our raw cybersecurity attack signatures (XSS & SQL Injection indicators)
        attack_signatures = ["<script>", "</script>", "javascript:",
                             "onclick", "onerror", "' OR '1'='1", "SELECT * FROM"]

        # Scan the input fields for malicious payloads
        for signature in attack_signatures:
            if signature.lower() in user_name.lower() or signature.lower() in user_comment.lower():
                is_attack = True
                break  # Stop loop immediately, payload confirmed

        # The Decision Fork
        if is_attack:
            # Drop everything, don't save to database, and freeze on the panic view
            context = {
                'is_attack': True,
                'error_message': "CRITICAL ACCESS DENIED // INTRUSION PREVENTION LOG ACTIVATED"
            }
            return render(request, 'korean_app/guestbook.html', context)
        else:
            # Text is safe! Store it directly inside our database table
            GuestbookEntry.objects.create(
                username=user_name, comment=user_comment)
            return redirect('guestbook')

    # If it's a standard page view (GET request), grab all messages from the database
    all_entries = GuestbookEntry.objects.all().order_by('-created_at')

    context = {
        'is_attack': is_attack,
        'entries': all_entries
    }
    return render(request, 'korean_app/guestbook.html', context)
