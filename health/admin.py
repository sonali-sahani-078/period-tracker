from django.contrib import admin  # Import this
from .models import Contact  # Make sure to import the model

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']  # Use list_display instead of clist

admin.site.register(Contact, ContactAdmin)
