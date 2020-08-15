# Generated by Django 3.0.5 on 2020-08-15 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_auto_20200814_2001'),
        ('appointment', '0003_auto_20200814_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_info', to='doctors.doctors_info'),
        ),
    ]