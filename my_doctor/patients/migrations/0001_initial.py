# Generated by Django 3.0.5 on 2020-08-04 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient_health_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=25, null=True)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('diabities', models.BooleanField()),
                ('blood_presure', models.BooleanField()),
                ('eye_sight', models.CharField(max_length=32, null=True)),
                ('phy_disabled', models.BooleanField()),
                ('other_deficiancy', models.CharField(max_length=25, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=25, null=True)),
                ('Last_modied', models.DateTimeField(auto_now_add=True)),
                ('Modified_by', models.CharField(max_length=25, null=True)),
            ],
        ),
    ]
