# Generated by Django 3.0.5 on 2020-09-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20200830_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='medical_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_history', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='patient_info',
            name='profile_pic',
            field=models.FileField(default='settings.MEDIA_ROOT/logos/anonymous-user.png', max_length=355, null=True, upload_to=''),
        ),
    ]