from django.shortcuts import render
from django.db import connection
# 1. Update your imports to include SecurityLog
from .models import Dictionary, SecurityLog


def dictionary_search(request):
    query_input = request.GET.get('q', '')
    security_mode = request.GET.get('mode', 'insecure')
    results = []
    executed_query = ""

    # New alert flag for our frontend template tray
    security_alert = False

    if query_input:
        if security_mode == 'insecure':
            # 2. CYBER ATTACK DETECTION TRIGGER
            # If the input contains a single quote or SQL comment dashes...
            if "'" in query_input or "--" in query_input:
                security_alert = True

                # Write a permanent record to our SecurityLog pantry shelf
                SecurityLog.objects.create(
                    attack_type="SQL Injection Attempt",
                    malicious_payload=query_input
                )

            # Your standard vulnerable execution code remains below:
            executed_query = f"SELECT id, korean_word, english_definition FROM korean_app_dictionary WHERE korean_word = '{query_input}'"
            with connection.cursor() as cursor:
                cursor.execute(executed_query)
                results = cursor.fetchall()
        else:
            # Secure execution route
            executed_query = "SELECT id, korean_word, english_definition FROM korean_app_dictionary WHERE korean_word = %s"
            with connection.cursor() as cursor:
                cursor.execute(executed_query, [query_input])
                results = cursor.fetchall()

    context = {
        'results': results,
        'query_input': query_input,
        'security_mode': security_mode,
        'executed_query': executed_query,
        'security_alert': security_alert,  # Passed to the layout plate
    }
    return render(request, 'korean_app/search.html', context)
