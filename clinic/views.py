from django.shortcuts import render, redirect
from django.core.serializers.json import DjangoJSONEncoder
import json
from .forms import ClinicRecordFormSet
from .models import Clinic_Record, Medicine
from django.contrib import messages



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
                        clinicForm.quantity = get_quantity

                        medicine_db.save()
                        clinicForm.save()

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




def clinic_report_details(request):
    clinics = Clinic_Record.objects.all()

    # itemFilter = ItemBaseFilter(request.GET, queryset=items)
    # items = itemFilter.qs
    # item_count = items.count()

    # if item_count > 0 :
    #     messages.info(request, f"Found '{item_count}' item(s) in the database")
    # else:
    #     messages.info(request, f"Item not Found in the database ")

    # #pagination show 50 items per page
    # paginator = Paginator(items, 25)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)

    # global filter_itembase_val
    # def filter_itembase_val():
    #     return items

    # # Compute Total Value
    # total_value = 0
    # for value in items:
    #     total_value += float(value.total_value)

    # # Compute Total Qty
    # total_soh = 0
    # for value in items:
    #     total_soh += int(value.soh)

    context = {
        'clinics': clinics,
        }
    return render(request, 'clinic/clinic_report_details.html', context)

