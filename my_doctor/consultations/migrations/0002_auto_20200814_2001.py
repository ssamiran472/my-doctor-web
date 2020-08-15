# Generated by Django 3.0.5 on 2020-08-14 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('consultations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultations',
            name='patient_id',
        ),
        migrations.AddField(
            model_name='consultations',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='consultations',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_consulataions', to='doctors.doctors_info'),
        ),
    ]