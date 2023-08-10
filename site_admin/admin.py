from django.contrib import admin
from .models import *

# Register your models here.
class AccomodationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'overview', 'address', 'status', 'created_at')
    list_filter = ('name', 'overview', 'address', 'status', 'created_at')
    list_per_page = 10
    search_fields = ('name', 'number_of_students', 'status', 'created_at')

admin.site.register(Accomodations, AccomodationsAdmin)
