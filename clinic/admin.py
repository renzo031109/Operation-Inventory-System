from django.contrib import admin
from .models import Location, Gender, Company, Illness, AMR, Medicine, Clinic_Record, Demand, MedicalServiceGiven, MedCode, MedicineMovement
admin.site.site_header = "S360 CLINIC"

# Registering other models as is
admin.site.register(Location)
admin.site.register(Gender)
admin.site.register(Company)
admin.site.register(Illness)
admin.site.register(AMR)
admin.site.register(Demand)
admin.site.register(MedicalServiceGiven)
# admin.site.register(Medicine)
admin.site.register(MedCode)
admin.site.register(MedicineMovement)


# Customizing the Clinic_Record admin view
@admin.register(Clinic_Record)
class ClinicRecordAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'last_name', 'first_name','department')  # Fields displayed in the admin list view
    search_fields = ('employee_id', 'last_name', 'first_name','department')  # Enables search functionality
    list_filter = ('gender', 'company')  # Optional: Filters for better usability


# # Customize Medicine admin
# @admin.register(Medicine)
# class MedicineAdmin(admin.ModelAdmin):
#     list_display = ('medicine', 'quantity')  # Columns displayed in the admin list view
#     search_fields = ('medicine',)  # Enables search functionality for the 'medicine' field






 
