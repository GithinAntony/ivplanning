from django.contrib import admin
from .models import *

# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('college_name', 'mobile_number', 'email', 'status', 'created_at')
    list_filter = ('college_name', 'mobile_number', 'email', 'status', 'created_at' )
    list_per_page = 10
    search_fields = ('college_name', 'mobile_number', 'email', 'created_at')

class Book_industryAdmin(admin.ModelAdmin):
    list_display = ('college', 'number_of_students', 'number_of_teachers', 'mobile_number','email','status', 'created_at')
    list_filter = ('college', 'number_of_students', 'number_of_teachers', 'mobile_number','email','status', 'created_at' )
    list_per_page = 10
    search_fields = ('college', 'number_of_students', 'mobile_number','email')

admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Book_industry, Book_industryAdmin)
admin.site.register(User_gallery)
