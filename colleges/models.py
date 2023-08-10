from django.db import models
from industry import models as industry_models
from django.utils.timezone import now

# Create your models here.
class Registration(models.Model):
    unique_id=models.AutoField(primary_key=True, null=False)
    college_name = models.CharField(max_length=255, default='null', null=False)
    website = models.CharField(max_length=500, default='null', null=False)
    land_phone = models.CharField(max_length=15, default='null', null=False)
    mobile_number = models.CharField(max_length=15, default='null', null=False)
    email = models.CharField(max_length=255, default='null', null=False)
    password = models.CharField(max_length=500, default='null', null=False)
    pincode = models.IntegerField(default=0, null=False )
    state = models.CharField(max_length=10,default='null', null=False )
    address = models.CharField(max_length=1000, default='null', null=False)
    about_college = models.TextField(default='null', null=False )
    profile_image = models.TextField(blank=True, null=True)
    status_choices = [
        ('pending', 'Pending'),
        ('active', 'Active'),
    ]
    status = models.CharField(max_length=15, choices=status_choices, default="active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    def __str__(self):
        return self.email

class User_gallery(models.Model):
    unique_id = models.AutoField(primary_key=True, null=False)
    college = models.ForeignKey(Registration,on_delete=models.SET_NULL,null=True)
    image = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return self.college.college_name

class Book_industry(models.Model):
    unique_id = models.AutoField(primary_key=True, null=False)
    college = models.ForeignKey(Registration,on_delete=models.CASCADE)
    industry = models.ForeignKey(industry_models.Registration,on_delete=models.CASCADE)
    cover_letter = models.CharField(max_length=3024, default='null', null=False)
    students_details = models.CharField(max_length=3024, default='null', null=False)
    number_of_students = models.IntegerField(default=0, null=False )
    number_of_teachers = models.IntegerField(default=0, null=False )
    mobile_number = models.CharField(max_length=15, default='null', null=False)
    email = models.CharField(max_length=255, default='null', null=False)
    status_choices = [
        ('requested', 'Requested'),
        ('cancelled', 'Cancelled'),
        ('accepted', 'Accepted'),
    ]
    status = models.CharField(max_length=15, choices=status_choices, default="requested")
    industry_response_letter = models.CharField(max_length=3024, default='', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name_plural = 'Industry Bookings'

    def __str__(self):
        return self.college.college_name

class Messages(models.Model):
    unique_id=models.AutoField(primary_key=True, null=False)
    industry_booking=models.ForeignKey(Book_industry, on_delete=models.CASCADE)
    colleges_user_id=models.IntegerField(default=0)
    industry_user_id = models.IntegerField(default=0)
    messages_text=models.TextField(default='null', null=False)
    date_added = models.DateTimeField(default=now, editable=False)
    status_choices = [
        ('colleges', 'Colleges'),
        ('industry', 'Industry'),
    ]
    status = models.CharField(max_length=15, choices=status_choices, default="colleges")

    def __str__(self):
        return self.messages_text

class Upload_Resume(models.Model):
    unique_id=models.AutoField(primary_key=True, null=False)
    firstname=models.CharField(max_length=255, default='', null=False)
    lastname=models.CharField(max_length=255, default='', null=False)
    mobile_number = models.CharField(max_length=15, default='', null=False)
    college = models.ForeignKey(Registration,on_delete=models.SET_NULL,null=True)
    industry = models.ForeignKey(industry_models.Registration,on_delete=models.CASCADE)
    industry_booking  = models.ForeignKey(Book_industry,on_delete=models.SET_NULL,null=True)
    resume=models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    def __str__(self):
        return self.firstname
