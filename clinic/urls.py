from django.urls import path
from . import views

urlpatterns = [
    path('step1/', views.clinic_record_step1, name='clinic_record_step1'),
    path('step2/', views.clinic_record_step2, name='clinic_record_step2'),
    path('success/', views.success, name='success'),
]