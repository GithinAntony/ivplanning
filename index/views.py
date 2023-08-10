from django.shortcuts import render, redirect
from industry.models import Registration as Industry_registraion, User_gallery as Industry_gallery
from colleges.models import Registration as College_registraion, Book_industry
from site_admin.models import *
from django.contrib import messages
from .models import *
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        data_record = request.POST
        contact = Contact_message(
        name=data_record['name'],
        phonenumber=data_record['phonenumber'],
        email=data_record['email'],
        message=data_record['message'],
        )
        contact.save()
        messages.success(request, 'Message added successfully!')
        return redirect('/contact')
    return render(request, 'contact.html')

def find_industry(request):
    datalist = Industry_registraion.objects.filter(status='active').all()
    context = { 'datalist': datalist }
    return render(request, 'find-industry.html', context)

def find_industry_view(request, id):
    datalist_1 =  {}
    if (request.session.get('is_logged_in') and request.session['usertype'] == 'colleges'):
        datalist_1 = Book_industry.objects.filter(college=College_registraion.objects.get(unique_id=request.session['user_id']),industry=Industry_registraion.objects.get(unique_id=id)).all()
    datalist= Industry_registraion.objects.get(unique_id=id)
    context = { 'datalist':datalist, 'datalist_1':datalist_1 }
    return render(request, 'find-industry-view.html', context)


def find_hotel(request):
    datalist = Accomodations.objects.filter(status='active').all()
    context = { 'datalist': datalist }
    return render(request, 'find-hotel.html', context)

def find_hotel_view(request, id):
    datalist= Accomodations.objects.get(id=id)
    context = { 'datalist':datalist }
    return render(request, 'find-hotel-view.html', context)
