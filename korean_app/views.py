from django.shortcuts import render
from django.db import connection
from .models import Dictionary


def dictionary_search(request):
    query_input = request.GET.get('q', '')
    # Captures our toggle switch state
    security_mode = request.GET.get('mode', 'insecure')
    results = []
    executed_query = ""

    if query_input:
        if security_mode == 'insecure':
            # VULNERABLE: Direct string interpolation allows SQL Injection!
            executed_query = f"SELECT id, korean_word, english_definition FROM korean_app_dictionary WHERE korean_word = '{query_input}'"

            with connection.cursor() as cursor:
                cursor.execute(executed_query)
                results = cursor.fetchall()  # Returns raw tuples
        else:
            # SECURE: Using parameterized queries isolates user input completely
            executed_query = "SELECT id, korean_word, english_definition FROM korean_app_dictionary WHERE korean_word = %s"

            with connection.cursor() as cursor:
                cursor.execute(executed_query, [query_input])
                results = cursor.fetchall()

    context = {
        'results': results,
        'query_input': query_input,
        'security_mode': security_mode,
        'executed_query': executed_query,
    }
    return render(request, 'korean_app/search.html', context)
