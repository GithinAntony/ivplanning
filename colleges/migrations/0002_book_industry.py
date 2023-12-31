# Generated by Django 4.0.4 on 2022-05-30 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_industry',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('cover_letter', models.CharField(default='null', max_length=3024)),
                ('students_details', models.CharField(default='null', max_length=3024)),
                ('number_of_students', models.IntegerField(default=0)),
                ('number_of_teachers', models.IntegerField(default=0)),
                ('mobile_number', models.CharField(default='null', max_length=15)),
                ('email', models.CharField(default='null', max_length=255)),
                ('status', models.CharField(choices=[('requested', 'Requested'), ('cancelled', 'Cancelled'), ('accepted', 'Accepted')], default='pending', max_length=15)),
                ('industry_response_letter', models.CharField(default='', max_length=3024, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.registration')),
            ],
            options={
                'verbose_name_plural': 'Industry Bookings',
            },
        ),
    ]
