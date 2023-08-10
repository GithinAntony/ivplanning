from django.db import models

# Create your models here.
class Contact_message(models.Model):
    unique_id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=True, verbose_name="Name")
    email = models.CharField(max_length=255, null=True, verbose_name="Email")
    phonenumber = models.CharField(max_length=10, null=True, verbose_name="Mobile Number")
    message = models.CharField(max_length=500, null=True, verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name_plural = 'Contact Messages'
        ordering = ('-created_at', )

    def __str__(self):
        return self.name
