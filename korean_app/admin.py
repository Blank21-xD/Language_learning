from django.contrib import admin
from .models import GuestbookEntry

@admin.register(GuestbookEntry)
class GuestbookEntryAdmin(admin.ModelAdmin):
    # This displays these columns neatly in a table layout inside the panel
    list_display = ('username', 'comment', 'created_at')
    
    # Adds a clickable search bar to quickly scan logs by user or text strings
    search_fields = ('username', 'comment')
    
    # Adds a sidebar filter pane to sort logs by submission date
    list_filter = ('created_at',)