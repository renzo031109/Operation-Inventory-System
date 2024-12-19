from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


def in_group(user, group_name): 
    return user.groups.filter(name=group_name).exists()


def is_clinic(user): 
    return in_group(user, 'Clinic')


@user_passes_test(is_clinic)
def clinic_form(request):
    context = {}
    return render(request, 'clinic/clinic_form.html', context)