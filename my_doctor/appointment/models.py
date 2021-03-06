from django.db import models
from django.contrib.auth.models import User
from doctors.models import doctors_info
from patients.models import patient_info
from rest_framework.reverse import reverse

class appointment(models.Model):
    appointment_date = models.CharField(max_length=32)
    appointment_time = models.CharField(max_length=32)
    doctor = models.ForeignKey(doctors_info,on_delete=models.CASCADE)
    patient = models.ForeignKey(User,related_name='appointments',on_delete=models.SET_NULL,null=True)
    Description = models.CharField(max_length=32, null=True)
    paid_amount = models.IntegerField()
    consultation_status = models.CharField(max_length=25, null=True)
    payment_type = models.CharField(max_length=25, null=True)
    payment_id = models.CharField(max_length=25, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=25, null=True)
    Last_modied = models.DateTimeField(auto_now_add=True)
    Modified_by = models.CharField(max_length=25, null=True)

    @property
    def patient_name(self):
        return patient_info.objects.get(user__id=self.patient.id).full_name
    
    @property
    def patient_age(self):
        return patient_info.objects.get(user__id=self.patient.id).age
    
    @property
    def patient_gender(self):
        return patient_info.objects.get(user__id=self.patient.id).gender
    

    def __str__(self):
        return str(self.id)
