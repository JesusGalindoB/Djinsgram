# Django
from django.contrib import admin

# Models
from .models import Profile

@admin.register(Profile)
class ProfielAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'website',
        'phone_number',
        'picture',
        'modified'
    )

    list_display_links = ('user', 'website')

    list_editable = ('phone_number', 'picture')

    fieldsets = (
        ('Profile', {
            'fields' : (('user', 'picture'),)
        }),
        ('Extra info', {
            'fields' : (
                ('website', 'phone_number'),
                'biography' 
            )
        }),
        ('Metadata', {
            'fields' : (('created_at', 'modified'),)
        }),
    )

    readonly_fields = ('created_at', 'modified')