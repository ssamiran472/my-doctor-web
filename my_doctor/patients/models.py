from django.db import models
from django.contrib.auth.models import User

class patient_info(models.Model):
    user = models.OneToOneField(User,related_name='patients',on_delete=models.CASCADE)
    pat_id = models.CharField(max_length=15,unique=True)
    full_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=25)
    dob = models.CharField(max_length=25,null=True)
    age = models.IntegerField(null=True)
    blood_group = models.CharField(max_length=5)
    rel_type = models.CharField(max_length=25,null=True)
    relation = models.CharField(max_length=32,null=True)
    ph_no=models.CharField(max_length=15)
    s_ph_no=models.CharField(max_length=15,null=True)
    pref_lang = models.CharField(max_length=25,null=True)
    street_address = models.CharField(max_length=200,null=True)
    locality = models.CharField(max_length=25,null=True)
    city = models.CharField(max_length=32,null=True)
    pincode=models.CharField(max_length=10,null=True)
    medical_history = models.CharField(max_length=1000,null=True)
    other_history=models.CharField(max_length=100,null=True)
    groups=models.CharField(max_length=200,null=True)
    profile_pic=models.FileField(max_length=355,null=True, default='settings.MEDIA_ROOT/logos/anonymous-user.png')
    height=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    weight=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    marital_status=models.CharField(max_length=20,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class medical_history(models.Model):
    medical_history=models.CharField(max_length=25)

    def __str__(self):
        return self.medical_history

class groups(models.Model):
    groups=models.CharField(max_length=25)

    def __str__(self):
        return self.groups