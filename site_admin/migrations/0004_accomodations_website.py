# Generated by Django 4.0.4 on 2022-06-02 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0003_alter_accomodations_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='accomodations',
            name='website',
            field=models.CharField(default='null', max_length=500, null=True),
        ),
    ]