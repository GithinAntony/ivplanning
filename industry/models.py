from django.db import models
from django.utils.timezone import now

# Create your models here.
class Registration(models.Model):
    unique_id=models.AutoField(primary_key=True, null=False)
    industry_name = models.CharField(max_length=255, default='null', null=False)
    website = models.CharField(max_length=500, default='null', null=False)
    land_phone = models.CharField(max_length=15, default='null', null=False)
    mobile_number = models.CharField(max_length=15, default='null', null=False)
    email = models.CharField(max_length=255, default='null', null=False)
    password = models.CharField(max_length=500, default='null', null=False)
    pincode = models.IntegerField(default=0, null=False )
    state = models.CharField(max_length=10,default='null', null=False )
    address = models.CharField(max_length=1000, default='null', null=False)
    about_industry = models.TextField(default='null', null=False )
    profile_image = models.TextField(blank=True, null=True)
    status_choices = [
        ('pending', 'Pending'),
        ('active', 'Active'),
    ]
    status = models.CharField(max_length=15, choices=status_choices, default="pending")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    def __str__(self):
        return self.email

class User_gallery(models.Model):
    unique_id = models.AutoField(primary_key=True, null=False)
    industry = models.ForeignKey(Registration,on_delete=models.SET_NULL,null=True)
    image = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return self.industry.industry_name
