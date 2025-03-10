from django.contrib import admin
from .models import Location, Gender, Company, Department, Illness, AMR, Medicine, Clinic_Record

admin.site.site_header = "S360 CLINIC"

# Registering other models as is
admin.site.register(Location)
admin.site.register(Gender)
admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Illness)
admin.site.register(AMR)

# Customizing the Clinic_Record admin view
@admin.register(Clinic_Record)
class ClinicRecordAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'last_name', 'first_name')  # Fields displayed in the admin list view
    search_fields = ('employee_id', 'last_name', 'first_name')  # Enables search functionality
    list_filter = ('gender', 'company', 'department')  # Optional: Filters for better usability


# Customize Medicine admin
@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'quantity')  # Columns displayed in the admin list view
    search_fields = ('medicine',)  # Enables search functionality for the 'medicine' field



 
