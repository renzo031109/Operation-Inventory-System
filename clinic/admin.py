from django.contrib import admin
from .models import Location, Gender, Company, Department, Illness, AMR, Medicine, Clinic_Record

admin.site.site_header = "S360 CLINIC"

admin.site.register(Location)
admin.site.register(Gender)
admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Illness)
admin.site.register(AMR)
admin.site.register(Medicine)
admin.site.register(Clinic_Record)



