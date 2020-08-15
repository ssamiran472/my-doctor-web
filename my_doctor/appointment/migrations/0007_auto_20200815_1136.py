# Generated by Django 3.0.5 on 2020-08-15 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_auto_20200815_1107'),
        ('appointment', '0006_auto_20200815_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctors_info'),
        ),
    ]