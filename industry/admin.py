from django.contrib import admin
from .models import *

# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('industry_name', 'mobile_number', 'email', 'status', 'created_at')
    list_filter = ('industry_name', 'mobile_number', 'email', 'status', 'created_at' )
    list_per_page = 10
    search_fields = ('industry_name', 'mobile_number', 'email', 'created_at')

admin.site.register(Registration, RegistrationAdmin)
admin.site.register(User_gallery)
