from django.contrib import admin
from .models import *

# Register your models here.
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phonenumber', 'created_at', 'updated_at')
    list_filter = ('name', 'email', 'phonenumber',)
    list_per_page = 10
    search_fields = ('name', 'email', 'phonenumber',)

admin.site.register(Contact_message, ContactMessageAdmin)
