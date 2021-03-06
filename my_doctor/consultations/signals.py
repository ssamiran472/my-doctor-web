from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from consultations.models import consultations
from doctor_payments.models import doctor_payments

@receiver(post_save, sender=consultations)
def save_doctor_payment(sender, instance, **kwargs):
    total_amount = doctor_payments.objects.filter(doctor = instance.doctor_id).values_list('total_amt',flat=True).first()
    commission_amount = doctor_payments.objects.filter(doctor = instance.doctor_id).values_list('comm_amt',flat=True).first()
    if instance.consultation_amt and instance.comp_share:
        if total_amount:
            total_amount = total_amount + instance.consultation_amt
        else:
            total_amount = instance.consultation_amt
        if commission_amount:
            commission_amount = commission_amount + instance.comp_share
        else:
            commission_amount = instance.comp_share
        payable = total_amount - commission_amount
    doc_count = consultations.objects.filter(doctor_id = instance.doctor_id).count()
    payments = doctor_payments.objects.filter(doctor = instance.doctor_id).update(total_amt=total_amount, consultations_count=doc_count, comm_amt=commission_amount, amount_payable=payable)
