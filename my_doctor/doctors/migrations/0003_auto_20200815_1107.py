# Generated by Django 3.0.5 on 2020-08-15 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_auto_20200814_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors_info',
            name='License',
        ),
        migrations.RemoveField(
            model_name='doctors_info',
            name='License_number',
        ),
    ]