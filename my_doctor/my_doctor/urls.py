from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('frontend.urls')),
    path('api/',include('accounts.urls')),
    path('api/',include('patients.urls')),
    path('api/',include('doctors.urls')),
    path('api/',include('specialist_type.urls')),
    path('api/',include('consultations.urls')),
    path('api/',include('appointment.urls')),
    path('api/',include('consultant_chat.urls')),
    path('api/',include('subscription_plans.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)