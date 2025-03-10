import django_filters
from django_filters import DateFilter, CharFilter, ChoiceFilter
from .models import Location, Gender, Company, Department, Illness, AMR, Medicine, Clinic_Record
from django import forms


#Location List
location = Location.objects.all()
location_list = []

for value in location:
    location_list.append((value.id, value.location))


#Gender List
gender = Gender.objects.all()
gender_list = []

for value in gender:
    gender_list.append((value.id, value.gender))


#Company List
company = Company.objects.all()
company_list = []

for value in company:
    company_list.append((value.id, value.company))


#Department List
department = Department.objects.all()
department_list = []

for value in department:
    department_list.append((value.id, value.department))


#Illness List
illness = Illness.objects.all()
illness_list = []

for value in illness:
    illness_list.append((value.id, value.illness))


#Amr List
amr = AMR.objects.all()
amr_list = []

for value in amr:
    amr_list.append((value.id, value.amr))


#Medicine List
medicine = Medicine.objects.all()
medicine_list = []

for value in medicine:
    medicine_list.append((value.id, value.medicine))



class DateInput(forms.DateInput):
    input_type = 'date'


class ClinicRecordFilter(django_filters.FilterSet):
    location = ChoiceFilter(field_name='location', label="LOCATION", choices=location_list)
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains', label="LASTNAME")
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains', label="FIRSTNAME")
    gender = ChoiceFilter(field_name='gender', label="GENDER", choices=gender_list)
    company = ChoiceFilter(field_name='company', label="COMPANY", choices=company_list)
    department = ChoiceFilter(field_name='department', label="DEPARTMENT", choices=department_list)
    illness = ChoiceFilter(field_name='illness', label="ILLNESS", choices=illness_list)
    amr = ChoiceFilter(field_name='amr', label="AMR", choices=amr_list)
    medicine = ChoiceFilter(field_name='medicine', label="MEDICINE", choices=medicine_list)
    date_from = DateFilter(field_name='date_added', lookup_expr='date__gte', label="DATE FROM", widget=DateInput(attrs={'type': 'date'}))
    date_to = DateFilter(field_name='date_added', lookup_expr='date__lte', label="DATE TO", widget=DateInput(attrs={'type': 'date'}))


    class Meta:
        model = Clinic_Record
        fields = ['location','last_name','first_name','gender','company','department','illness','amr','medicine','date_from','date_to']
        


class MedicineFilter(django_filters.FilterSet):
    medicine = CharFilter(field_name='medicine', lookup_expr='icontains', label="MEDICINE")
    

    class Meta:
        model = Medicine
        fields = ['medicine']
