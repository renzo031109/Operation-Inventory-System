from django import forms
from .models import Clinic_Record


class ClinicRecordFormStep1(forms.ModelForm):
    class Meta:
        model = Clinic_Record
        fields = [
            'location', 
            'employee_id', 
            'last_name',
            'first_name',
            'gender',
            'company',
            'department']
        
        labels = {
            'location': 'LOCATION',
            'employee_id': 'EMPLOYEE ID',
            'last_name': 'LAST NAME',
            'first_name': 'FIRST NAME',
            'gender': 'GENDER',
            'company': 'COMPANY',
            'department': 'DEPARTMENT'
        }

        widgets = {
            'location': forms.Select(attrs={'class':'ClinicRecordForm', 'autocomplete': 'off'}),
            'employee_id': forms.TextInput(attrs={'class':'ClinicRecordForm','autocomplete': 'off'}),
            'first_name': forms.TextInput(attrs={'class':'ClinicRecordForm', 'autocomplete': 'off'}),
            'last_name': forms.TextInput(attrs={'class':'ClinicRecordForm', 'autocomplete': 'off'}),
            'gender': forms.Select(attrs={'class':'ClinicRecordForm', 'autocomplete': 'off'}),
            'company': forms.Select(attrs={'class':'ClinicRecordForm', 'autocomplete': 'off'}),
            'department': forms.Select(attrs={'class':'ClinicRecordForm', 'autocomplete': 'off'}),
        }


class ClinicRecordFormStep2(forms.ModelForm):
    class Meta:
        model = Clinic_Record
        fields = [
            'illness',
            'amr',
            'medicine']

        labels = {
            'illness': 'ILLNESS',
            'amr': 'AMR',
            'medicine': 'MEDICINE'
        }

        widgets = {  
            'illness': forms.Select(attrs={'class':'ClinicRecordForm', 'autocomplete': 'off'}),
            'amr': forms.Select(attrs={'class':'ClinicRecordForm', 'autocomplete': 'off'}),
            'medicine': forms.Select(attrs={'class':'ClinicRecordForm', 'autocomplete': 'off'})
        }    

