from django.urls import path
from . import views

urlpatterns = [
    path('clinic_records/', views.clinic_record_steps, name='clinic_record_steps'),
    path('clinic_report_details/', views.clinic_report_details, name='clinic_report_details'),
    path('medicine_report_details/', views.medicine_report_details, name='medicine_report_details'),
    path('clinic_export_excel_summary/', views.clinic_export_excel_summary, name='clinic_export_excel_summary'),
    path('medicine_export_excel_summary/', views.medicine_export_excel_summary, name='medicine_export_excel_summary'),
    path('success/', views.success, name='success'),
    path('add_medicine/', views.add_medicine, name='add_medicine'),
    path('new_medicine/', views.new_medicine, name='new_medicine'),
]