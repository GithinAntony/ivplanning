from django.db import models

# Create your models here.
class Accomodations(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=200, null=True)
    overview = models.TextField(null=True)
    description = models.TextField(null=True)
    amenities = models.CharField(max_length=250, null=True)
    besttime = models.CharField(max_length=150, null=True)
    howtoreach = models.CharField(max_length=250, null=True)
    address = models.TextField(null=True)
    latitude = models.CharField(max_length=50, null=True)
    longitude = models.CharField(max_length=50, null=True)
    website = models.CharField(max_length=500, default='null', null=True)    
    status_choices = [
        ('pending', 'Pending'),
        ('active', 'Active'),
    ]
    status = models.CharField(max_length=15, choices=status_choices, default="active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    def __str__(self):
        return self.name
