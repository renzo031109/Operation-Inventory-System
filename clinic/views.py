from django.shortcuts import render, redirect
from django.core.serializers.json import DjangoJSONEncoder
import json
from .forms import ClinicRecordFormStep1, ClinicRecordFormStep2
from .models import Clinic_Record, Location, Gender, Company, Department, Illness, AMR, Medicine

def clinic_record_step1(request):
    if request.method == 'POST':
        form = ClinicRecordFormStep1(request.POST)
        if form.is_valid():
            clinical_record_data_step1 = form.cleaned_data
            # Serialize the data before saving it to the session
            clinical_record_data_step1_serializable = {
                'location': clinical_record_data_step1['location'].id if clinical_record_data_step1['location'] else None,
                'employee_id': clinical_record_data_step1['employee_id'],
                'last_name': clinical_record_data_step1['last_name'],
                'first_name': clinical_record_data_step1['first_name'],
                'gender': clinical_record_data_step1['gender'].id if clinical_record_data_step1['gender'] else None,
                'company': clinical_record_data_step1['company'].id if clinical_record_data_step1['company'] else None,
                'department': clinical_record_data_step1['department'].id if clinical_record_data_step1['department'] else None,
            }
            request.session['clinical_record_data_step1'] = json.dumps(clinical_record_data_step1_serializable, cls=DjangoJSONEncoder)
            return redirect('clinic_record_step2')
    else:
        form = ClinicRecordFormStep1()
    return render(request, 'clinic/clinic_record_step1.html', {'form': form})

def clinic_record_step2(request):
    if request.method == 'POST':
        form = ClinicRecordFormStep2(request.POST)
        if form.is_valid():
            # Deserialize the data from the session
            clinical_record_data_step1_serializable = json.loads(request.session.get('clinical_record_data_step1', '{}'))
            clinical_record_data_step2 = form.cleaned_data
            clinical_record_data = {
                'location': clinical_record_data_step1_serializable['location'],
                'employee_id': clinical_record_data_step1_serializable['employee_id'],
                'last_name': clinical_record_data_step1_serializable['last_name'],
                'first_name': clinical_record_data_step1_serializable['first_name'],
                'gender': clinical_record_data_step1_serializable['gender'],
                'company': clinical_record_data_step1_serializable['company'],
                'department': clinical_record_data_step1_serializable['department'],
                'illness': clinical_record_data_step2['illness'].id if clinical_record_data_step2['illness'] else None,
                'amr': clinical_record_data_step2['amr'].id if clinical_record_data_step2['amr'] else None,
                'medicine': clinical_record_data_step2['medicine'].id if clinical_record_data_step2['medicine'] else None,
            }
            # Create the Clinic_Record object
            Clinic_Record.objects.create(
                location=Location.objects.get(id=clinical_record_data['location']) if clinical_record_data['location'] else None,
                employee_id=clinical_record_data['employee_id'],
                last_name=clinical_record_data['last_name'],
                first_name=clinical_record_data['first_name'],
                gender=Gender.objects.get(id=clinical_record_data['gender']) if clinical_record_data['gender'] else None,
                company=Company.objects.get(id=clinical_record_data['company']) if clinical_record_data['company'] else None,
                department=Department.objects.get(id=clinical_record_data['department']) if clinical_record_data['department'] else None,
                illness=Illness.objects.get(id=clinical_record_data['illness']) if clinical_record_data['illness'] else None,
                amr=AMR.objects.get(id=clinical_record_data['amr']) if clinical_record_data['amr'] else None,
                medicine=Medicine.objects.get(id=clinical_record_data['medicine']) if clinical_record_data['medicine'] else None,
            )
            return redirect('success')
    else:
        form = ClinicRecordFormStep2()
    return render(request, 'clinic/clinic_record_step2.html', {'form': form})

def success(request):
    return render(request, 'clinic/success.html')
