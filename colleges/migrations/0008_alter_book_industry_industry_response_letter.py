# Generated by Django 4.0.4 on 2022-06-02 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0007_upload_resume_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_industry',
            name='industry_response_letter',
            field=models.CharField(default='null', max_length=3024, null=True),
        ),
    ]
