# Generated by Django 3.0.5 on 2020-09-19 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultant_chat', '0003_auto_20200918_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultant_chat',
            name='attached_file',
            field=models.FileField(max_length=355, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='consultant_chat',
            name='message',
            field=models.CharField(max_length=2500, null=True),
        ),
    ]