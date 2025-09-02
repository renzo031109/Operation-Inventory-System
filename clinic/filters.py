import django_filters
from django_filters import DateFilter, CharFilter, ChoiceFilter
from .models import Location, Gender, Company, Illness, AMR, Medicine, Clinic_Record
from django_filters import ModelChoiceFilter
from django import forms





class DateInput(forms.DateInput):
    input_type = 'date'


class ClinicRecordFilter(django_filters.FilterSet):
    location =  ModelChoiceFilter(field_name='location', label="LOCATION", queryset=Location.objects.all())
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains', label="LASTNAME")
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains', label="FIRSTNAME")
    gender = ModelChoiceFilter(field_name='gender', label="GENDER", queryset=Gender.objects.all())
    company = ModelChoiceFilter(field_name='company', label="COMPANY", queryset=Company.objects.all())
    department = CharFilter(field_name='department', lookup_expr='icontains', label="CLIENT/DEPARTMENT")
    illness = ModelChoiceFilter(field_name='illness', label="ILLNESS", queryset=Illness.objects.all())
    amr = ModelChoiceFilter(field_name='amr', label="AMR", queryset=AMR.objects.all())
    medicine = ModelChoiceFilter(field_name='medicine', label="MEDICINE",  queryset=Medicine.objects.all())
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


    
class MedicineMovementFilter(django_filters.FilterSet):
    medicine = CharFilter(field_name='medicine', lookup_expr='icontains', label="MEDICINE")
    

    class Meta:
        model = Medicine
        fields = ['medicine']
