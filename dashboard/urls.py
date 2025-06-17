from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('critical_stock_excel_export/', views.critical_stock_excel_export, name='critical_stock_excel_export'),
    path('critical_medicine_excel_export/', views.critical_medicine_excel_export, name='critical_medicine_excel_export'),
    

]
