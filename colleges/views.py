from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from industry.models import Registration as Industry_registraion, User_gallery as Industry_gallery
from .models import Registration, User_gallery, Book_industry,Upload_Resume, Messages as User_messages
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
                    request.session['college_name'] = user_details.college_name
                    request.session['user_id'] = user_details.unique_id
                    request.session['mobile_number'] = user_details.mobile_number
                    request.session['usertype'] = 'colleges'
                    return redirect('/colleges/dashboard')
                else:
                    messages.error(request, 'User is suspended. Contact the admin!')
                    return redirect('/colleges/login')
            else:
                messages.error(request, 'Invalid credentials!')
                return redirect('/colleges/login')
    return render(request, 'colleges/login.html')

def signup(request):
    if request.method == 'POST':
        data_record = request.POST
        if Registration.objects.filter(email=data_record['email_address']):
            messages.error(request, 'Email already exists! Please try again!')
            return redirect('/colleges/signup')
        elif Registration.objects.filter(mobile_number=data_record['mobile_number']):
            messages.error(request, 'Mobile number already exists! Please try again!')
            return redirect('/colleges/signup')
        else:
            uploaded_file = request.FILES['change_avatar']
            fs = FileSystemStorage()
            file_name = fs.save("PROFILE_"+uploaded_file.name, uploaded_file)
            signup = Registration(
            college_name=data_record['college_name'],
            website=data_record['website'],
            land_phone=data_record['land_phone'],
            mobile_number=data_record['mobile_number'],
            email=data_record['email_address'],
            state=data_record['state'],
            password=data_record['password'],
            pincode=data_record['pincode'],
            address=data_record['address'],
            about_college=data_record['about_college'],
            profile_image=fs.url(file_name),
            status='pending',
            )
            signup.save()
            messages.success(request, 'College registered successfully!')
            return redirect('/colleges/login')
    context = {}
    return render(request, 'colleges/signup.html', context)

def logout(request):
    del request.session['is_logged_in']
    del request.session['college_name']
    del request.session['email']
    del request.session['user_id']
    del request.session['mobile_number']
    del request.session['usertype']
    return redirect('/colleges/login')

def dashboard(request):
    if not (request.session.get('is_logged_in')):
        return redirect('/colleges/login')
    userdata = Registration.objects.get(unique_id=request.session['user_id'])
    context = { 'userdata': userdata }
    return render(request, 'colleges/dashboard.html', context)

def edit_profile(request):
    if not (request.session.get('is_logged_in')):
        return redirect('/colleges/login')
    userdata = Registration.objects.get(unique_id=request.session['user_id'])
    if request.method == 'POST':
        data_record = request.POST
        if Registration.objects.filter(email=data_record['email_address']).exclude(unique_id=request.session['user_id']):
            messages.error(request, 'Email already exists! Please try again!')
            return redirect('colleges/edit-profile')
        else:
            try:
                uploaded_file = request.FILES['change_avatar']
                fs = FileSystemStorage()
                file_name = fs.save("PROFILE_"+uploaded_file.name, uploaded_file)
                userdata.profile_image = fs.url(file_name)
            except MultiValueDictKeyError:
                filepath = False
            userdata.college_name = data_record['college_name']
            userdata.website = data_record['website']
            userdata.land_phone = data_record['land_phone']
            userdata.mobile_number = data_record['mobile_number']
            userdata.email = data_record['email_address']
            userdata.state = data_record['state']
            userdata.pincode = data_record['pincode']
            userdata.address = data_record['address']
            userdata.about_college = data_record['about_college']
            userdata.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('/colleges/edit-profile')
    context = { 'userdata': userdata }
    return render(request, 'colleges/edit-profile.html', context)

def change_password(request):
    if not (request.session.get('is_logged_in')):
        return redirect('/colleges/login')
    userdata = Registration.objects.get(unique_id=request.session['user_id'])
    if request.method == 'POST':
        data_record = request.POST
        if userdata.password == data_record['old_password']:
            userdata.password = data_record['password']
            userdata.save()
            messages.success(request, 'Password updated successfully!')
        else:
            messages.error(request, 'Please enter correct previous password!')
        return redirect('/colleges/change-password')
    return render(request, 'colleges/change-password.html')


def gallery(request):
    if not (request.session.get('is_logged_in')):
        return redirect('/colleges/login')
    user_gallery = User_gallery.objects.filter(college=Registration.objects.get(unique_id=request.session['user_id']))
    if request.method == 'POST':
            uploaded_file = request.FILES['main_photo']
            fs = FileSystemStorage()
            file_name = fs.save(uploaded_file.name, uploaded_file)
            user_gallery = User_gallery(
                college=Registration.objects.get(unique_id=request.session['user_id']),
                image=fs.url(file_name),
            )
            user_gallery.save()
            messages.success(request, 'Image added successfully')
            return redirect('/colleges/gallery')
    context = { 'user_gallery': user_gallery }
    return render(request, 'colleges/gallery.html', context)

def gallery_delete(request,id):
    User_gallery.objects.filter(unique_id=id).delete()
    messages.error(request, 'Image deleted!')
    return redirect('/colleges/gallery')

def book_industry(request,id):
    if not (request.session.get('is_logged_in')):
        return redirect('/colleges/login')
    if request.method == 'POST':
        data_record = request.POST
        book_industry = Book_industry(
        college = Registration.objects.get(unique_id=request.session['user_id']),
        industry = Industry_registraion.objects.get(unique_id=id),
        cover_letter=data_record['cover_letter'],
        students_details=data_record['students_details'],
        number_of_students=data_record['number_of_students'],
        number_of_teachers=data_record['number_of_teachers'],
        mobile_number=data_record['contact_mobile_number'],
        email=data_record['contact_email_address'],
        status='requested',
        )
        book_industry.save()
        messages.success(request, 'Industry booked successfully!')
        return redirect('/find-industry')
    datalist= Industry_registraion.objects.get(unique_id=id)
    datalist_gallery = Industry_gallery.objects.filter(industry=datalist).all()
    context = { 'datalist':datalist, 'datalist_gallery': datalist_gallery }
    return render(request, 'colleges/book-industry.html', context)

def view_industry(request,id,industry_id):
    if not (request.session.get('is_logged_in')):
        return redirect('/colleges/login')
    booking_details = Book_industry.objects.get(unique_id=id)
    if request.method == 'POST':
        data_record = request.POST
        booking_details.cover_letter = data_record['cover_letter']
        booking_details.students_details = data_record['students_details']
        booking_details.number_of_students = data_record['number_of_students']
        booking_details.number_of_teachers = data_record['number_of_teachers']
        booking_details.mobile_number = data_record['contact_mobile_number']
        booking_details.email = data_record['contact_email_address']
        booking_details.save()
        messages.success(request, 'Industry booking edited successfully!')
        return redirect('/colleges/view-industry/'+str(id)+'/'+str(industry_id))
    user_messages = User_messages.objects.filter(industry_booking=booking_details).all()
    datalist= Industry_registraion.objects.get(unique_id=industry_id)
    datalist_gallery = Industry_gallery.objects.filter(industry=datalist).all()
    context = { 'datalist':datalist, 'datalist_gallery': datalist_gallery, 'booking_details':booking_details, 'user_messages': user_messages, }
    return render(request, 'colleges/view-industry.html', context)

def delete_industry(request,id):
    if not (request.session.get('is_logged_in')):
        return redirect('/colleges/login')
    Book_industry.objects.get(unique_id=id).delete()
    messages.error(request, 'Booking deleted!')
    return redirect('/find-industry')

def add_messages(request,id,industry_id):
    if request.method == 'POST':
        data_record = request.POST
        mess_app = User_messages(
        messages_text=data_record['message'],
        industry_booking=Book_industry.objects.get(unique_id=id),
        colleges_user_id=request.session['user_id'],
        industry_user_id=0,
        status=request.session['usertype'],
        )
        mess_app.save()
        messages.success(request, 'Messages Added')
    return redirect('/colleges/view-industry/'+str(id)+'/'+str(industry_id))

def upload_resume(request,id,industry_id):
    booking_details = Book_industry.objects.get(unique_id=id)
    if request.method == 'POST':
        data_record = request.POST
        uploaded_file = request.FILES['upload_resume']
        fs = FileSystemStorage()
        file_name = fs.save("RESUME_"+uploaded_file.name, uploaded_file)
        resume_upload = Upload_Resume(
        firstname=data_record['firstname'],
        lastname=data_record['lastname'],
        mobile_number=data_record['mobile_number'],
        college_id=request.session['user_id'],
        industry_id=industry_id,
        industry_booking_id=id,
        resume=fs.url(file_name),
        )
        resume_upload.save()
        messages.success(request, 'Resume uploaded successfully!')
        return redirect('/colleges/upload-resume/'+str(id)+'/'+str(industry_id))
    datalist=Upload_Resume.objects.filter(industry_booking=booking_details).all()
    context = { 'datalist':datalist }
    return render(request, 'colleges/upload-resume.html', context)

def delete_resume(request,id, industry_booking_id, industry_id):
    if not (request.session.get('is_logged_in')):
        return redirect('/colleges/login')
    Upload_Resume.objects.get(unique_id=id).delete()
    messages.error(request, 'Resume deleted!')
    return redirect('/colleges/upload-resume/'+str(industry_booking_id)+'/'+str(industry_id))
