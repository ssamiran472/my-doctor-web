from .serializers import consultationsSerializer,getAllConsultationsSerializer
from .models import consultations
from rest_framework import viewsets, permissions , mixins
from doctors.models import doctors_info


class consultationsViewSet(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = consultationsSerializer

    def get_queryset(self):
        return consultations.objects.all()

    # def perform_create(self, serializer):
    #     print(self.request.data)
    #     doctor = doctors_info.objects.get(id=self.request.data['doctor_id'])
    #     cons_fee = self.request.data['consultation_amt']
    #     share_type = doctor.commission_type
    #     share_val = doctor.commission_val
    #     if share_type == 'Pencent':
    #         share_val = cons_fee * (share_val/100)
    #     serializer.save(patient=self.request.user,comp_share=share_val)

class getAllConsultations(mixins.ListModelMixin, viewsets.GenericViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = getAllConsultationsSerializer

    def get_queryset(self):
        return consultations.objects.all()

class getPatientConsultations(mixins.ListModelMixin, viewsets.GenericViewSet):
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = getAllConsultationsSerializer

    def get_queryset(self):
         print(self.request.user.consultations.all())
         return self.request.user.consultations.all()

class getDoctorConsultations(mixins.ListModelMixin, viewsets.GenericViewSet):
    
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = getAllConsultationsSerializer
   
    def get_queryset(self):
        return consultations.objects.filter(doctor_id__user=self.request.user)