from django import forms
from .models import Clinic_Record, MedicineNew, Medicine, MedicalServiceGiven
from django.forms import modelformset_factory


#Formset for Get Item

class ClinicRecordFormSteps(forms.ModelForm):
    class Meta:
        model = Clinic_Record
        fields = [
            'location', 
            'employee_id', 
            'last_name',
            'first_name',
            'gender',
            'company',
            'department',
            'illness',
            'amr',
            'medical_given',
            'note',
            'medicine',
            'quantity',
            
            ]
        
        
        labels = {
            'location': 'CLINIC LOCATION',
            'employee_id': 'EMPLOYEE ID',
            'last_name': 'LAST NAME',
            'first_name': 'FIRST NAME',
            'gender': 'GENDER',
            'company': 'COMPANY',
            'department': 'CLIENT/DEPARTMENT',
            'illness': 'CHIEF COMPLAINT OR ILLNESS OR CONSULTATION MEDICAL DIAGNOSIS',
            'amr': 'AMR LIST OF DISEASES',
            'medical_given': 'MEDICAL SERVICE GIVEN (NURSE TO FILL UP)',
            'note':'NOTE',
            'medicine': '',
            'quantity': ''
        }

        widgets={
            'location': forms.Select(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True}),
            'employee_id': forms.TextInput(attrs={'class':'ClinicRecordFormSteps','autocomplete': 'off', 'required': True}),
            'last_name': forms.TextInput(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True}),
            'first_name': forms.TextInput(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True}),       
            'gender': forms.Select(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True}),
            'company': forms.Select(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True}),
            'department': forms.Select(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True}),
            'illness': forms.Select(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True}),
            'amr': forms.Select(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True}),
            'medical_given': forms.Select(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True }),
            'note': forms.Textarea(attrs={'rows': 2, 'cols': 50}),
            'medicine': forms.Select(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True }),
            'quantity': forms.TextInput(attrs={'class':'ClinicRecordFormSteps','autocomplete': 'off', 'required': True }),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


ClinicRecordFormSet = modelformset_factory(Clinic_Record, form=ClinicRecordFormSteps, extra=1)



class AddMedicineForm(forms.ModelForm):
    class Meta:
        model = MedicineNew
        fields = [
            'medicine',
            'quantity'
            ]
        
        
        labels = {
            'medicine': '',
            'quantity': ''
        }

        widgets={
            'medicine': forms.Select(attrs={'class':'AddMedicineForm', 'autocomplete': 'off', 'required': True }),
            'quantity': forms.TextInput(attrs={'class':'AddMedicineForm','autocomplete': 'off', 'required': True }),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


MedicineRecordFormSet = modelformset_factory(MedicineNew, form=AddMedicineForm, extra=1)



class NewMedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = [
            'medicine',
            'quantity',
            'demand',
            'critical'
            ]
        
        
        labels = {
            'demand':'',
            'critical': '',
            'medicine': '',
            'quantity': ''
        }

        widgets={

            'medicine': forms.TextInput(attrs={'class':'NewMedicineForm','autocomplete': 'off', 'required': True }),
            'quantity': forms.TextInput(attrs={'class':'NewMedicineForm','autocomplete': 'off', 'required': True }),
            'demand': forms.Select(attrs={'class':'NewMedicineForm', 'autocomplete': 'off', 'required': True }),
            'critical': forms.TextInput(attrs={'class':'NewMedicineForm','autocomplete': 'off', 'required': True }),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


NewMedicineRecordFormSet = modelformset_factory(Medicine, form=NewMedicineForm, extra=1)