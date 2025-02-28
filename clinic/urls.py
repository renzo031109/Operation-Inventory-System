from django.urls import path
from . import views

urlpatterns = [
    path('clinic_records/', views.clinic_record_steps, name='clinic_record_steps'),
    path('clinic_report_details/', views.clinic_report_details, name='clinic_report_details'),
    path('success/', views.success, name='success'),
]