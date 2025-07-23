from django.contrib import admin
from .models import Note

# PUBLIC_INTERFACE
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """Admin for Note objects."""
    list_display = ('title', 'owner', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'owner__username')

