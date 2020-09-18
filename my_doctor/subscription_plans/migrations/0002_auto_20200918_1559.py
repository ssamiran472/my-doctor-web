# Generated by Django 3.0.5 on 2020-09-18 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription_plans', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription_plans',
            name='Modified_by',
        ),
        migrations.RemoveField(
            model_name='subscription_plans',
            name='created_by',
        ),
        migrations.AddField(
            model_name='subscription_plans',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='subscription_plans',
            name='icon',
            field=models.FileField(max_length=355, null=True, upload_to=''),
        ),
    ]
