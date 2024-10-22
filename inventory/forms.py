from django import forms
from django.forms import modelformset_factory, BaseFormSet
from .models import Item, ItemBase, Floor, ItemCode

        
class ItemNewForm(forms.ModelForm):
    class Meta:
        model = ItemBase
        fields = [
            'site',
            'item_name',
            'brand_name',
            'soh','uom',
            # 'price',
            'item_code',
            'remarks',
            'critical_value',
            'demand_item',
            'division'
            ]
        labels = {
            'site': 'SITE',
            'item_name': 'ITEM NAME',
            'brand_name': 'BRAND NAME (NONE if N/A)',
            'soh': 'BEGINNING BALANCE',
            # 'price': 'PRICE',
            'item_code': 'ITEM CODE',
            'uom':'UOM',
            'remarks' : 'REMARKS',
            'critical_value': 'CRITICAL VALUE',
            'demand_item': 'DEMAND ITEM',
            'division': 'DIVISION'

        }
        widgets = {
            'site': forms.Select(attrs={'class':'ItemNewForm', 'autocomplete': 'off'}),
            'item_name': forms.TextInput(attrs={'class':'ItemNewForm','autocomplete': 'off'}),
            'brand_name': forms.TextInput(attrs={'class':'ItemNewForm', 'value':'NONE', 'autocomplete': 'off'}),
            'soh': forms.TextInput(attrs={'class':'ItemNewForm', 'autocomplete': 'off'}),
            'uom': forms.Select(attrs={'class':'ItemNewForm', 'autocomplete': 'off'}),
            # 'price': forms.TextInput(attrs={'class':'ItemNewForm', 'autocomplete': 'off'}),
            'item_code': forms.TextInput(attrs={'class':'ItemNewForm','autocomplete': 'off','type':'hidden'}),
            'remarks': forms.TextInput(attrs={'value': 'OUT', 'type':'hidden'}),
            'critical_value': forms.TextInput(attrs={'class':'ItemNewForm', 'autocomplete': 'off'}),
            'demand_item': forms.Select(attrs={'class':'ItemNewForm', 'autocomplete': 'off'}),
            'division': forms.Select(attrs={'class':'ItemNewForm', 'autocomplete': 'off'}),
        }


#Formset for Get Item

class ItemGetForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'item_code',
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
            ]
        
        labels = {
            # 'firstName':'FIRST NAME',
            # 'middleName': 'MIDDLE NAME',
            # 'lastName': 'LAST NAME',
            # 'client_name': 'CLIENT NAME',
            # 'dapartment_name': 'DEPARTMENT NAME',
            'member': 'STAFF NAME',
            'site': 'SITE',
            'floor': 'FLOOR',
            'purpose': 'PURPOSE'
        }

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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['floor'].queryset = Floor.objects.none()
        self.fields['item_code'].queryset = ItemCode.objects.none()

        print("this site", self.data)

        if 'form-0-site' in self.data:
            try:
                site_id = int(self.data.get('form-0-site'))
                self.fields['floor'].queryset = Floor.objects.filter(site_id=site_id).order_by('floor')
                self.fields['item_code'].queryset = ItemCode.objects.filter(site_id=site_id).order_by('code')
            except (ValueError, TypeError):
                pass # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['floor'].queryset = self.instance.site.floor_set.order_by('floor')
            self.fields['item_code'].queryset = self.instance.site.itemcode_set.order_by('code')




        

class ItemAddForm(forms.ModelForm):
    class Meta:
        model = Item

        fields=(
        'site',
        'item_code',
        'quantity',
        'item_name',
        'brand_name',
        'staff_name',
        # 'client_name',
        # 'department_name',
        # 'price'   
        )

        labels={
        'site': 'SITE',
        'staff_name': 'STAFF NAME',
        # 'client_name': 'CLIENT NAME',
        # 'dapartment_name': 'DEPARTMENT NAME',
        # 'price': 'PRICE'
        
        }

        widgets={
        'site': forms.Select(attrs={
            'class':'form-control form-select',
            'autocomplete': 'off',
            'placeholder':"SITE",
            'required':True,
            }),
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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customizing the empty label for a select field
        self.fields['site'].empty_label = "*** Please select SITE ***"
        self.fields['item_code'].empty_label = "******"
        self.fields['item_code'].queryset = ItemCode.objects.none()

        #this will populate accdg to user choices on site
        if 'form-0-site' in self.data:
            try:
                site_id = int(self.data.get('form-0-site'))
                self.fields['item_code'].queryset = ItemCode.objects.filter(site_id=site_id).order_by('code')
            except (ValueError, TypeError):
                pass # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['item_code'].queryset = self.instance.site.item_code_set.order_by('code')


# modelformset functions

ItemModelFormSet = modelformset_factory(Item, form=ItemGetForm, extra=1) 

ItemModelFormSetAdd = modelformset_factory(Item, form=ItemAddForm, extra=1)



