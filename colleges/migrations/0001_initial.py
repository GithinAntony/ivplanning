# Generated by Django 4.0.1 on 2022-05-15 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('college_name', models.CharField(default='null', max_length=255)),
                ('website', models.CharField(default='null', max_length=500)),
                ('land_phone', models.CharField(default='null', max_length=15)),
                ('mobile_number', models.CharField(default='null', max_length=15)),
                ('email', models.CharField(default='null', max_length=255)),
                ('password', models.CharField(default='null', max_length=500)),
                ('pincode', models.IntegerField(default=0)),
                ('state', models.CharField(default='null', max_length=10)),
                ('address', models.CharField(default='null', max_length=1000)),
                ('about_college', models.TextField(default='null')),
                ('profile_image', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Active')], default='pending', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
            ],
        ),
        migrations.CreateModel(
            name='User_gallery',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.TextField(blank=True, null=True)),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='colleges.registration')),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
    ]
