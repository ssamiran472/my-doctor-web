from django.db import models
from django.contrib.auth.models import User

class doctors_info(models.Model):
    user = models.OneToOneField(User,related_name='Doctors',on_delete=models.CASCADE)
    full_name=models.CharField(max_length=32,null=True)
    phone_number = models.CharField(max_length=15,null=True)
    commission_val=models.DecimalField(max_digits=10,decimal_places=2,default=2)
    commission_type=models.CharField(max_length=15,default='Percent')
    Registration_Number = models.CharField(max_length=25, null=True)
    specialist_type = models.CharField(max_length=25, null=True)
    rating = models.IntegerField(default=0)
    consultation_fee = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    profile_pic = models.FileField(max_length=355, null=True)
    mou_file = models.FileField(null=True)
    about  = models.CharField(max_length=500, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=25, null=True)
    Last_modied = models.DateTimeField(auto_now=True)
    Modified_by = models.CharField(max_length=25, null=True)
    

    def __str__(self):
        return str(self.full_name) +','+ str(self.specialist_type)


class DoctorTimings(models.Model):
    doctor=models.ForeignKey(doctors_info,related_name="timings",on_delete=models.CASCADE)
    mon=models.BooleanField()
    tue=models.BooleanField()
    wed=models.BooleanField()
    thu=models.BooleanField()
    fri=models.BooleanField()
    sat=models.BooleanField()
    sun=models.BooleanField()
    from_time=models.CharField(max_length=50)
    to_time=models.CharField(max_length=50)

    def __str__(self):
        return self.doctor.full_name