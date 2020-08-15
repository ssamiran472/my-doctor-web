# Generated by Django 3.0.5 on 2020-08-10 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='specialist_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special_type', models.CharField(max_length=25, null=True)),
                ('icon', models.CharField(max_length=25, null=True)),
                ('is_acrive', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=32, null=True)),
                ('Last_modied', models.DateTimeField(auto_now_add=True)),
                ('Modified_by', models.CharField(max_length=25, null=True)),
            ],
        ),
    ]