from django import forms
from django.forms import modelformset_factory, BaseFormSet
from .models import Item, ItemBase

        
class ItemNewForm(forms.ModelForm):
    class Meta:
        model = ItemBase
        fields = [
            'item_name',
            'brand_name',
            'soh','uom',
            # 'price',
            'item_code',
            'remarks',
            'critical_value'
            ]
        labels = {
            'item_name': 'ITEM NAME',
            'brand_name': 'BRAND NAME (NONE if N/A)',
            'soh': 'BEGINNING BALANCE',
            # 'price': 'PRICE',
            'item_code': 'ITEM CODE',
            'uom':'UOM',
            'remarks' : 'REMARKS',
            'critical_value': 'CRITICAL VALUE'

        }
        widgets = {
            'item_name': forms.TextInput(attrs={'class':'ItemNewForm','autocomplete': 'off'}),
            'brand_name': forms.TextInput(attrs={'class':'ItemNewForm', 'value':'NONE', 'autocomplete': 'off'}),
            'soh': forms.TextInput(attrs={'class':'ItemNewForm', 'autocomplete': 'off'}),
            'uom': forms.Select(attrs={'class':'ItemNewForm', 'autocomplete': 'off'}),
            # 'price': forms.TextInput(attrs={'class':'ItemNewForm', 'autocomplete': 'off'}),
            'item_code': forms.TextInput(attrs={'class':'ItemNewForm','autocomplete': 'off','type':'hidden'}),
            'remarks': forms.TextInput(attrs={'value': 'OUT', 'type':'hidden'}),
            'critical_value': forms.TextInput(attrs={'class':'ItemNewForm', 'autocomplete': 'off'})
        }


#Formset for Get Item
ItemModelFormSet = modelformset_factory(
    Item, 
    fields=('item_code',
            'quantity','item_name',
            'brand_name',
            # 'client_name',
            # 'department_name',
            # 'firstName',
            # 'lastName',
            # 'middleName',
            'member',
            'site',
            'floor',
            'purpose'
            ),
    extra=1,
    labels={
        # 'firstName':'FIRST NAME',
        # 'middleName': 'MIDDLE NAME',
        # 'lastName': 'LAST NAME',
        # 'client_name': 'CLIENT NAME',
        # 'dapartment_name': 'DEPARTMENT NAME',
        'member': 'STAFF NAME',
        'site': 'SITE',
        'floor': 'FLOOR',
        'purpose': 'PURPOSE'

    },
    widgets={
        'item_code': forms.Select(attrs={
            'class':'form-control form-select',
            'autocomplete': 'off',
            'required':True
            }),
        'quantity': forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': '0',
            'autocomplete': 'off',
            'required':True
            }),
        'remarks': forms.TextInput(attrs={
            'class':'form-control',
            'type':'hidden'
            }),
        'item_name': forms.TextInput(attrs={
            'class':'form-control',
            'type':'hidden'
            }),
        'brand_name': forms.TextInput(attrs={
            'class':'form-control',
            'type':'hidden'
            }),
        # 'firstName': forms.TextInput(attrs={
        #     'class':'form-control',
        #     }),
        # 'middleName': forms.TextInput(attrs={
        #     'class':'form-control', 
        #     }),
        # 'lastName': forms.TextInput(attrs={
        #     'class':'form-control', 
        #     }),
        'staff_name': forms.TextInput(attrs={
            'class':'form-control',
            'type':'hidden'
            }),
        # 'client_name': forms.Select(attrs={
        #     'class':'form-control',
        #     }),
        # 'department_name': forms.Select(attrs={
        #     'class':'form-control',    
        #     }),
        'member': forms.Select(attrs={
            'class':'form-control',    
            }),
        'site': forms.Select(attrs={
            'class':'form-control',    
            }),
        'floor': forms.Select(attrs={
            'class':'form-control',    
            }),
        'purpose': forms.TextInput(attrs={
            'class':'form-control',
            }),
  

    }
)


#Formset for Add Item
ItemModelFormSetAdd = modelformset_factory(
    Item, 
    fields=(
        'item_code',
        'quantity',
        'item_name',
        'brand_name',
        'staff_name',
        # 'client_name',
        # 'department_name',
        # 'price'
        ),
    extra=1,
    labels={
        'staff_name': 'STAFF NAME',
        # 'client_name': 'CLIENT NAME',
        # 'dapartment_name': 'DEPARTMENT NAME',
        # 'price': 'PRICE'
    },
    widgets={
        'item_code': forms.Select(attrs={
            'class':'form-control form-select',
            'autocomplete': 'off',
            'required':True
            }),
        'quantity': forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': '0',
            'autocomplete': 'off',
            'id':'id_add_form-0-quantity',
            'required':True
            }),
        'remarks': forms.TextInput(attrs={
            'class':'form-control',
            'type':'hidden'
            }),
        'item_name': forms.TextInput(attrs={
            'class':'form-control',
            'type':'hidden'
            }),
        'brand_name': forms.TextInput(attrs={
            'class':'form-control',
            'type':'hidden'
            }),
        'staff_name': forms.TextInput(attrs={
            'class':'form-control',
     
            }),
        # 'client_name': forms.Select(attrs={
        #     'class':'form-control',
        #     }),
        # 'department_name': forms.Select(attrs={
        #     'class':'form-control',
       
        #     }),
        # 'price': forms.TextInput(attrs={
        #     'class':'form-control',
        #     'required':True
        #     }),

    }
)

