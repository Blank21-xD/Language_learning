from django.shortcuts import render, redirect
from django.db import connection
from .models import Category, Vocabulary, UserProfilereview, GuestbookEntry
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
    return render(request, 'korean_app/slang.html')


def guestbook(request):
    is_attack = False

    if request.method == "POST":
        user_name = request.POST.get("username", "")
        user_comment = request.POST.get("comment", "")

        attack_signatures = ["<script>", "</script>", "javascript:",
                             "onclick", "onerror", "' OR '1'='1", "SELECT * FROM"]

        for signature in attack_signatures:
            if signature.lower() in user_name.lower() or signature.lower() in user_comment.lower():
                is_attack = True
                break

        if is_attack:
            # 1. Extract metadata forensics from the request headers
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip_address = x_forwarded_for.split(',')[0]
            else:
                ip_address = request.META.get('REMOTE_ADDR', 'UNKNOWN_IP')

            user_agent = request.META.get('HTTP_USER_AGENT', 'UNKNOWN_BROWSER')

            # 2. Fire a loud, formatted warning log directly into the server terminal console
            print("\n" + "="*60, file=sys.stderr)
            print("🚨 INTRUSION DETECTION SYSTEM (IDS) ALERT 🚨", file=sys.stderr)
            print(f"SOURCE IP    : {ip_address}", file=sys.stderr)
            print(f"USER-AGENT   : {user_agent}", file=sys.stderr)
            print(
                f"VIOLATION    : Malicious payload intercepted in form fields.", file=sys.stderr)
            print(
                f"FLAGGED DATA : Name='{user_name}' | Comment='{user_comment}'", file=sys.stderr)
            print("="*60 + "\n", file=sys.stderr)

            context = {
                'is_attack': True,
                'error_message': "CRITICAL ACCESS DENIED // INTRUSION PREVENTION LOG ACTIVATED"
            }
            return render(request, 'korean_app/guestbook.html', context)

        else:
            GuestbookEntry.objects.create(
                username=user_name, comment=user_comment)
            return redirect('guestbook')

    all_entries = GuestbookEntry.objects.all().order_by('-created_at')
    context = {
        'is_attack': is_attack,
        'entries': all_entries
    }
    return render(request, 'korean_app/guestbook.html', context)
