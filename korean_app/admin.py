from django.contrib import admin
from .models import Category, Vocabulary, UserProfilereview, GuestbookEntry, SecurityIncidentLog

# This tells Django: "Hey, show these tables in the Admin dashboard!"


@admin.register(SecurityIncidentLog)
class SecurityIncidentLogAdmin(admin.ModelAdmin):
    list_display = ('attacker_ip', 'flagged_username', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('attacker_ip', 'flagged_username')
    readonly_fields = ('attacker_ip', 'user_agent',
                       'flagged_username', 'flagged_comment', 'timestamp')


# Register your other models too
admin.site.register(Category)
admin.site.register(Vocabulary)
admin.site.register(UserProfilereview)
admin.site.register(GuestbookEntry)
