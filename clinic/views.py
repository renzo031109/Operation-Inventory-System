from django.shortcuts import render, redirect
from django.core.serializers.json import DjangoJSONEncoder
import json
from .forms import ClinicRecordFormSet, MedicineRecordFormSet, NewMedicineRecordFormSet
from .models import Clinic_Record, Medicine
from django.contrib import messages
from .filters import ClinicRecordFilter, MedicineFilter
from django.http import HttpResponse

#for export excel imports
from openpyxl.styles.borders import Border, Side, BORDER_THIN
from openpyxl import Workbook
from datetime import datetime
from openpyxl.styles import *
from urllib.parse import quote


def success(request):
    return render(request, 'clinic/success.html')


def clinic_record_steps(request):

    location_list = []
    employee_id_list = []
    last_name_list = []
    first_name_list = []
    gender_list = []
    company_list = []
    department_list = []
    illness_list = []
    amr_list = []
    insufficient_quantity = False

    if request.method == 'POST':
        formset = ClinicRecordFormSet(request.POST)

        if formset.is_valid():

            for form in formset:

                if form.cleaned_data.get('medicine') and form.cleaned_data.get('quantity'):

                    #get the input of user
                    get_location = form.cleaned_data.get('location')
                    get_employee_id = form.cleaned_data.get('employee_id')
                    get_last_name = form.cleaned_data.get('last_name')
                    get_first_name = form.cleaned_data.get('first_name')
                    get_gender = form.cleaned_data.get('gender')
                    get_company = form.cleaned_data.get('company')
                    get_department = form.cleaned_data.get('department')
                    get_illness = form.cleaned_data.get('illness')
                    get_amr = form.cleaned_data.get('amr')
                    get_medicine = form.cleaned_data.get('medicine')
                    get_quantity = form.cleaned_data.get('quantity')

                    #connect the Medicine DB
                    medicine_db = Medicine.objects.get(medicine=get_medicine)
                    
                    if medicine_db.quantity > get_quantity:
                        
                        #deduct the quantity of the medicine
                        new_quantity = medicine_db.quantity - get_quantity
                        medicine_db.quantity = new_quantity

                        #add the input to a list
                        location_list.append(get_location)
                        employee_id_list.append(get_employee_id)
                        last_name_list.append(get_last_name)
                        first_name_list.append(get_first_name)
                        gender_list.append(get_gender)
                        company_list.append(get_company)
                        department_list.append(get_department)
                        illness_list.append(get_illness)
                        amr_list.append(get_amr)

                        #assign the first form value
                        location = location_list[0]
                        employee_id =  employee_id_list[0]
                        last_name = last_name_list[0]
                        first_name = first_name_list[0]
                        gender = gender_list[0]
                        company = company_list[0]
                        department = department_list[0]
                        illness = illness_list[0]
                        amr = amr_list[0]


                        #Convert qty value to negative for get
                        qtyToNegative = (get_quantity ) * -1

                        #hold save
                        clinicForm = form.save(commit=False)
                
                        #assign the value to the fields db
                        clinicForm.location = location
                        clinicForm.employee_id =  employee_id
                        clinicForm.last_name = last_name
                        clinicForm.first_name = first_name
                        clinicForm.gender = gender
                        clinicForm.company = company
                        clinicForm.department = department
                        clinicForm.illness = illness
                        clinicForm.amr = amr 
                        clinicForm.medicine = get_medicine
                        clinicForm.quantity = qtyToNegative

                        clinicForm.save()

                        medicine_db.save()

                    else:
                        insufficient_quantity = True          
                        messages.error(request, f"Unable to process, insufficient quantity for {get_medicine}")


            if insufficient_quantity:
                return render(request, 'clinic/clinic_record_steps.html', {'formset': formset})
            return redirect('success')

        else:
            
            messages.error(request, "Invalid Input!")
            
    else:
        formset = ClinicRecordFormSet(queryset=Clinic_Record.objects.none())

    context = {'formset': formset}
    return render(request, 'clinic/clinic_record_steps.html', context)



def add_medicine(request):

    # #Initiate a list variable for the input select fields
    # site_name_list = []

    if request.method == 'POST':
        formset = MedicineRecordFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                
                # check if itemcode is selected
                if form.cleaned_data.get('medicine') and form.cleaned_data.get('quantity'):  
                    
                    #get the item name from the form 
                    add_medicine = form.cleaned_data.get('medicine')

                    #get the item qty from the form
                    add_qty = form.cleaned_data.get('quantity')

                    
                    medicine_soh = Medicine.objects.get(medicine=add_medicine)

                    #compute add soh
                    soh = int(medicine_soh.quantity) + int(add_qty)

                    #get the updated soh after add
                    medicine_soh.quantity = int(soh)
                    
                    #save tables
                    medicine_soh.save()
                        
                
                else:

                    messages.error(request, "Invalid Input. Form is incomplete.")
                    return redirect('add_medicine')
                
            messages.success(request, "You added stock successfully!")
                
            return redirect('medicine_report_details')
        
        else:
            messages.error(request, "Invalid Input!")

    else:
        formset = MedicineRecordFormSet(queryset=Medicine.objects.none())

    context = {'formset': formset}
    return render(request, 'clinic/add_medicine.html', context)



def new_medicine(request):

    if request.method == 'POST':
        formset = NewMedicineRecordFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
            
                # Get values from the form
                new_medicine = form.cleaned_data.get('medicine')  # Use cleaned_data for safety
                new_medicine_qty = form.cleaned_data.get('quantity')

                # Check if value exist in the database
                if Medicine.objects.filter(medicine__iexact=new_medicine).exists():
                    messages.error(request, f"The value '{new_medicine}' already exists in the database. Please enter a different value.")
                    return render(request, 'clinic/new_medicine.html', {'formset': formset})
         
                # Check if fields are valid
                if new_medicine and new_medicine_qty:
                    # Create and save the new medicine entry
                    new_medicine_db = Medicine(medicine=new_medicine, quantity=new_medicine_qty)
                    new_medicine_db.save()
                    messages.success(request, "You added stock successfully!")
                else:
                    # Add an error message for incomplete fields
                    messages.error(request, "Both medicine and quantity fields are required.")
                    return redirect('new_medicine')
                
            return redirect('medicine_report_details')
        else:
            messages.error(request, "Invalid Input!")

    else:
        formset = NewMedicineRecordFormSet(queryset=Medicine.objects.none())

    context = {'formset': formset}
    return render(request, 'clinic/new_medicine.html', context)



def clinic_report_details(request):
    clinic = Clinic_Record.objects.all()

    clinic_record_filter = ClinicRecordFilter(request.GET, queryset=clinic)
    clinics = clinic_record_filter.qs
    item_count = clinics.count()

    #Prompt a message on the qty of the listed report
    if item_count > 0 :
        messages.info(request, f"Found '{item_count}' item(s) in the database")
    else:
        messages.info(request, f"Item not Found in the database ")


    #This will send the variable to filter views
    global filter_clinic_record_val
    def filter_clinic_record_val():
        return clinics


    context = {
        'item_count': item_count,
        'clinics': clinics,
        'clinic_record_filter': clinic_record_filter
        }
    return render(request, 'clinic/clinic_report_details.html', context)



def medicine_report_details(request):
    medicine = Medicine.objects.all()

    medicine_record_filter = MedicineFilter(request.GET, queryset=medicine)
    medicines = medicine_record_filter.qs
    item_count = medicines.count()

    #Prompt a message on the qty of the listed report
    if item_count > 0 :
        messages.info(request, f"Found '{item_count}' item(s) in the database")
    else:
        messages.info(request, f"Item not Found in the database ")


    #This will send the variable to filter views
    global filter_medicine_record_val
    def filter_medicine_record_val():
        return medicines


    context = {
        'item_count': item_count,
        'medicines': medicines,
        'clinic_record_filter': medicine_record_filter
        }
    return render(request, 'clinic/medicine_report.html', context)



def clinic_export_excel_summary(request):

    #Export excel function
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="CLINICAL LOGS.xlsx"'

    thin_border = Border(left=Side(style='thin'), 
                     right=Side(style='thin'), 
                     top=Side(style='thin'), 
                     bottom=Side(style='thin'))


    # Declare Workbook
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.merge_cells('A1:L1')

    first_cell = worksheet['A1']
    first_cell.value = "CLINICAL LOGS"
    first_cell.font = Font(bold=True)
    first_cell.alignment = Alignment(horizontal="center", vertical="center")


    worksheet.title = "CLINICAL LOGS"

    # Add headers
    headers =   [
                'LOCATION',	
                'EMPLOYEE ID',
                'NAME'
                'GENDER',
                'COMPANY',
                'DEPARTMENT/CLIENT',
                'CHIEF COMPLAINT',
                'BODY SYSTEM',
                'MEDICINE',
                'QUANTITY',
                'DATE'
                ]
    row_num = 2


    for col_num, column_title in enumerate(headers, 1):
        cell = worksheet.cell(row=row_num, column=col_num)
        cell.value = column_title
        cell.fill = PatternFill("solid", fgColor="CFE2FF")
        cell.font = Font(bold=True, color="0B5ED7")
        cell.border = thin_border


    # Add data from the model
    # items = ItemBase.objects.all()
    # check if it was filtered if not set default to all
    if filter_clinic_record_val():
        clinics = filter_clinic_record_val()
        print("With filter value")
    else:
        clinics = Clinic_Record.objects.all()
        print("filter no value")

    for item in clinics:
        
        #convert object fields to string

        location = str(item.location)
        employee = str(item.employee_id)
        gender = str(item.gender)
        name = str(item.first_name+ ' ' + item.last_name)
        gender = str(item.gender)
        company = str(item.company)
        department = str(item.department)
        illness = str(item.illness)
        amr = str(item.amr)
        medicine = str(item.medicine)
        quantity = str(item.quantity)
        date_added = datetime.strftime(item.date_added,'%m/%d/%Y %H:%M:%S')


        worksheet.append([
            location,
            employee,
            gender,
            name,
            gender,
            company,
            department,
            illness,
            amr,
            medicine,
            quantity,
            date_added
        ])
    
    workbook.save(response)
    return response



def medicine_export_excel_summary(request):

    #Export excel function
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="MEDICINE LOGS.xlsx"'

    thin_border = Border(left=Side(style='thin'), 
                     right=Side(style='thin'), 
                     top=Side(style='thin'), 
                     bottom=Side(style='thin'))


    # Declare Workbook
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.merge_cells('A1:B1')

    first_cell = worksheet['A1']
    first_cell.value = "MEDICINE LOGS"
    first_cell.font = Font(bold=True)
    first_cell.alignment = Alignment(horizontal="center", vertical="center")


    worksheet.title = "MEDICINE LOGS"

    # Add headers
    headers =   [
                'MEDICINE',
                'QUANTITY',
                ]
    row_num = 2


    for col_num, column_title in enumerate(headers, 1):
        cell = worksheet.cell(row=row_num, column=col_num)
        cell.value = column_title
        cell.fill = PatternFill("solid", fgColor="CFE2FF")
        cell.font = Font(bold=True, color="0B5ED7")
        cell.border = thin_border


    # Add data from the model
    # items = ItemBase.objects.all()
    # check if it was filtered if not set default to all
    if filter_medicine_record_val():
        medicines = filter_medicine_record_val()
        print("With filter value")
    else:
        medicines = Medicine.objects.all()
        print("filter no value")

    for item in medicines:
        
        #convert object fields to string

        medicine = str(item.medicine)
        quantity = str(item.quantity)

        worksheet.append([
            medicine,
            quantity,
        ])
    
    workbook.save(response)
    return response









