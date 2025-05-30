from django import forms
from .models import Clinic_Record, MedicineNew, Medicine, MedicalServiceGiven, MedCode, Location
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
            'medcode',
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
            'amr': 'BODY SYSTEM AFFECTED',
            'medical_given': 'MEDICAL SERVICE GIVEN (NURSE TO FILL UP)',
            'note':'NOTE',
            'medcode': '',
            'quantity': ''
        }

        widgets={
            'location': forms.Select(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True}),
            'employee_id': forms.TextInput(attrs={'class':'ClinicRecordFormSteps','autocomplete': 'off', 'required': True}),
            'last_name': forms.TextInput(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True}),
            'first_name': forms.TextInput(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True}),       
            'gender': forms.Select(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True}),
            'company': forms.Select(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True}),
            'department': forms.TextInput(attrs={'class':'ClinicRecordFormSteps','autocomplete': 'off', 'required': True}),
            'illness': forms.Select(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True}),
            'amr': forms.Select(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True}),
            'medical_given': forms.Select(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True }),
            'note': forms.Textarea(attrs={'rows': 2, 'cols': 50, 'required': False }),
            'medcode': forms.Select(attrs={'class':'ClinicRecordFormSteps', 'autocomplete': 'off', 'required': True }),
            'quantity': forms.TextInput(attrs={'class':'ClinicRecordFormSteps','autocomplete': 'off', 'required': True }),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medcode'].queryset = MedCode.objects.none()

        print('this location ', self.data)

        #this will populate accdg to user choices on location
        if 'form-0-location' in self.data:
            try:
                location_id = int(self.data.get('form-0-location'))
                self.fields['medcode'].queryset = MedCode.objects.filter(location_id=location_id).order_by('code')
            except (ValueError, TypeError):
                pass #invalid input from the client
        elif self.instance.pk:
            self.fields['medcode'].queryset = self.instance.location.medcode_set.order_by('code')


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
            'location',
            'medicine',
            'quantity',
            'demand',
            'critical'
            ]
        
        
        labels = {
            'location':'',
            'demand':'',
            'critical': '',
            'medicine': '',
            'quantity': ''
        }

        widgets={
            'location': forms.Select(attrs={'class':'NewMedicineForm', 'autocomplete': 'off', 'required': True }),
            'medicine': forms.TextInput(attrs={'class':'NewMedicineForm','autocomplete': 'off', 'required': True }),
            'quantity': forms.TextInput(attrs={'class':'NewMedicineForm','autocomplete': 'off', 'required': True }),
            'demand': forms.Select(attrs={'class':'NewMedicineForm', 'autocomplete': 'off', 'required': True }),
            'critical': forms.TextInput(attrs={'class':'NewMedicineForm','autocomplete': 'off', 'required': True }),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


NewMedicineRecordFormSet = modelformset_factory(Medicine, form=NewMedicineForm, extra=1)