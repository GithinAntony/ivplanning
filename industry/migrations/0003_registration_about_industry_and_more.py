# Generated by Django 4.0.1 on 2022-05-15 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industry', '0002_alter_registration_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='about_industry',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='registration',
            name='profile_image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
