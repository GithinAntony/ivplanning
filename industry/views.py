from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from colleges.models import Registration as Colleges_registraion, Book_industry, Messages as User_Messages, Upload_Resume
from .models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.

def login(request):
    if request.method == 'POST':
            data_record = request.POST
            if Registration.objects.filter(email=data_record['email_address'],password=data_record['password']):
                user_details = Registration.objects.get(email=data_record['email_address'],password=data_record['password'])
                if user_details.status == 'active':
                    request.session['is_logged_in'] = True
                    request.session['email'] = user_details.email
                    request.session['industry_name'] = user_details.industry_name
                    request.session['user_id'] = user_details.unique_id
                    request.session['mobile_number'] = user_details.mobile_number
                    request.session['usertype'] = 'industry'
                    return redirect('/industry/dashboard')
                else:
                    messages.error(request, 'User is suspended. Contact the admin!')
                    return redirect('/industry/login')
            else:
                messages.error(request, 'Invalid credentials!')
                return redirect('/industry/login')
    return render(request, 'industry/login.html')

def signup(request):
    if request.method == 'POST':
        data_record = request.POST
        if Registration.objects.filter(email=data_record['email_address']):
            messages.error(request, 'Email already exists! Please try again!')
            return redirect('/industry/signup')
        elif Registration.objects.filter(mobile_number=data_record['mobile_number']):
            messages.error(request, 'Mobile number already exists! Please try again!')
            return redirect('/industry/signup')
        else:
            uploaded_file = request.FILES['change_avatar']
            fs = FileSystemStorage()
            file_name = fs.save("PROFILE_"+uploaded_file.name, uploaded_file)
            signup = Registration(
            industry_name=data_record['industry_name'],
            website=data_record['website'],
            land_phone=data_record['land_phone'],
            mobile_number=data_record['mobile_number'],
            email=data_record['email_address'],
            state=data_record['state'],
            password=data_record['password'],
            pincode=data_record['pincode'],
            address=data_record['address'],
            about_industry=data_record['about_industry'],
            profile_image=fs.url(file_name),
            status='pending',
            )
            signup.save()
            messages.success(request, 'User registered successfully!')
            return redirect('/industry/login')
    context = {}
    return render(request, 'industry/signup.html', context)

def logout(request):
    del request.session['is_logged_in']
    del request.session['industry_name']
    del request.session['email']
    del request.session['user_id']
    del request.session['mobile_number']
    del request.session['usertype']
    return redirect('/industry/login')

def dashboard(request):
    if not (request.session.get('is_logged_in')):
        return redirect('/industry/login')
    userdata = Registration.objects.get(unique_id=request.session['user_id'])
    context = { 'userdata': userdata }
    return render(request, 'industry/dashboard.html', context)

def edit_profile(request):
    if not (request.session.get('is_logged_in')):
        return redirect('/industry/login')
    userdata = Registration.objects.get(unique_id=request.session['user_id'])
    if request.method == 'POST':
        data_record = request.POST
        if Registration.objects.filter(email=data_record['email_address']).exclude(unique_id=request.session['user_id']):
            messages.error(request, 'Email already exists! Please try again!')
            return redirect('industry/edit-profile')
        else:
            try:
                uploaded_file = request.FILES['change_avatar']
                fs = FileSystemStorage()
                file_name = fs.save("PROFILE_"+uploaded_file.name, uploaded_file)
                userdata.profile_image = fs.url(file_name)
            except MultiValueDictKeyError:
                filepath = False
            userdata.industry_name = data_record['industry_name']
            userdata.website = data_record['website']
            userdata.land_phone = data_record['land_phone']
            userdata.mobile_number = data_record['mobile_number']
            userdata.email = data_record['email_address']
            userdata.state = data_record['state']
            userdata.pincode = data_record['pincode']
            userdata.address = data_record['address']
            userdata.about_industry = data_record['about_industry']
            userdata.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('/industry/edit-profile')
    context = { 'userdata': userdata }
    return render(request, 'industry/edit-profile.html', context)

def change_password(request):
    if not (request.session.get('is_logged_in')):
        return redirect('/industry/login')
    userdata = Registration.objects.get(unique_id=request.session['user_id'])
    if request.method == 'POST':
        data_record = request.POST
        if userdata.password == data_record['old_password']:
            userdata.password = data_record['password']
            userdata.save()
            messages.success(request, 'Password updated successfully!')
        else:
            messages.error(request, 'Please enter correct previous password!')
        return redirect('/industry/change-password')
    return render(request, 'industry/change-password.html')

def gallery(request):
    if not (request.session.get('is_logged_in')):
        return redirect('/industry/login')
    user_gallery = User_gallery.objects.filter(industry=Registration.objects.get(unique_id=request.session['user_id']))
    if request.method == 'POST':
            uploaded_file = request.FILES['main_photo']
            fs = FileSystemStorage()
            file_name = fs.save(uploaded_file.name, uploaded_file)
            user_gallery = User_gallery(
                industry=Registration.objects.get(unique_id=request.session['user_id']),
                image=fs.url(file_name),
            )
            user_gallery.save()
            messages.success(request, 'Image added successfully')
            return redirect('/industry/gallery')
    context = { 'user_gallery': user_gallery }
    return render(request, 'industry/gallery.html', context)

def gallery_delete(request,id):
    User_gallery.objects.filter(unique_id=id).delete()
    messages.error(request, 'Image deleted!')
    return redirect('/industry/gallery')

def iv_requests(request):
    datalist= Book_industry.objects.filter(industry=Registration.objects.get(unique_id=request.session['user_id'])).all()
    context = { 'datalist': datalist }
    return render(request, 'industry/iv-requests.html', context)

def iv_requests_view(request,id):
    if not (request.session.get('is_logged_in')):
        return redirect('/colleges/login')
    booking_details = Book_industry.objects.get(unique_id=id)
    if request.method == 'POST':
        data_record = request.POST
        booking_details.industry_response_letter = data_record['response_letter']
        booking_details.status = data_record['change_status']
        booking_details.save()
        messages.success(request, 'Response added successfully!')
        return redirect('/industry/iv-requests-view/'+str(id))
    user_messages = User_Messages.objects.filter(industry_booking=booking_details).all()
    context = { 'booking_details':booking_details, 'user_messages': user_messages, }
    return render(request,'industry/iv-requests-view.html',context)


def add_messages(request, id):
    if request.method == 'POST':
        data_record = request.POST
        mess_app= User_Messages(
        messages_text=data_record['message'],
        industry_booking=Book_industry.objects.get(unique_id=id),
        colleges_user_id=0,
        industry_user_id=request.session['user_id'],
        status=request.session['usertype'],
        )
        mess_app.save()
        messages.success(request, 'Message Added')
    return redirect('/industry/iv-requests-view/'+str(id))

def view_resume(request,id):
    booking_details = Book_industry.objects.get(unique_id=id)
    datalist=Upload_Resume.objects.filter(industry_booking=booking_details).all()
    context = { 'datalist':datalist }
    return render(request, 'industry/view-resume.html', context)
