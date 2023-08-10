# Generated by Django 4.0.4 on 2022-05-31 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accomodations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('overview', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('amenities', models.CharField(max_length=250, null=True)),
                ('besttime', models.CharField(max_length=150, null=True)),
                ('howtoreach', models.CharField(max_length=250, null=True)),
                ('address', models.TextField(null=True)),
                ('latitude', models.CharField(max_length=50, null=True)),
                ('longitude', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Active')], default='pending', max_length=15)),
            ],
        ),
    ]
