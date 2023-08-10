# Generated by Django 4.0.4 on 2022-05-31 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0004_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_Resume',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(default='', max_length=255)),
                ('lastname', models.CharField(default='', max_length=255)),
                ('resume', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
            ],
        ),
        migrations.AlterField(
            model_name='registration',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('active', 'Active')], default='active', max_length=15),
        ),
    ]