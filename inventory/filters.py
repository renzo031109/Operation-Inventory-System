import django_filters
from django_filters import DateFilter, CharFilter, ChoiceFilter
from .models import Item, ItemBase, Site, Floor, TeamMember, DemandItems, Division
from django import forms


remarks_select = (
    ('IN', 'IN'),
    ('OUT', 'OUT'),
    ('BEGINNING','BEGINNING')
)

# #department list
# departments = Department.objects.all()
# departments_list = []

# #get department values
# for value in departments:
#     departments_list.append((value.id, value.department))

#Site List
site = Site.objects.all()
site_list = []

for value in site:
    site_list.append((value.id, value.site))

# #client list
# clients = Client.objects.all()
# clients_list = []

# #get client values
# for value in clients:
#     clients_list.append((value.id, value.client))


#Floor List
floor = Floor.objects.all()
floor_list = []

for value in floor:
    floor_list.append((value.id, value.floor))


#Member List
member = TeamMember.objects.all()
member_list = []

for value in member:
    member_list.append((value.id, value.member))


 #Demand Item List
demand_item = DemandItems.objects.all()
demand_item_list = []

for value in demand_item:
    demand_item_list.append((value.id, value.demand_item))

#Division List
division = Division.objects.all()
division_list = []

for value in division:
    division_list.append((value.id, value.division))




class DateInput(forms.DateInput):
    input_type = 'date'


class ItemFilter(django_filters.FilterSet):
    item_name = CharFilter(field_name='item_name', lookup_expr='icontains', label="ITEM NAME")
    brand_name = CharFilter(field_name='brand_name', lookup_expr='icontains', label="BRAND NAME")
    remarks = ChoiceFilter(field_name='remarks', label="REMARKS", choices=remarks_select)
    date_from = DateFilter(field_name='date_added', lookup_expr='date__gte', label="DATE FROM", widget=DateInput(attrs={'type': 'date'}))
    date_to = DateFilter(field_name='date_added', lookup_expr='date__lte', label="DATE TO", widget=DateInput(attrs={'type': 'date'}))
    member = ChoiceFilter(field_name='member', label="STAFF NAME", choices=member_list)
    # department= ChoiceFilter(field_name='department_name', label="DEPARTMENT", choices=departments_list)
    # client= ChoiceFilter(field_name='client_name', label="CLIENT", choices=clients_list)
    site = ChoiceFilter(field_name='site', label="SITE", choices=site_list)
    floor = ChoiceFilter(field_name='floor', label="FLOOR", choices=floor_list)
    division = ChoiceFilter(field_name='division', label="DIVISION", choices=division_list)

   
    class Meta:
        model = Item
        fields = ['item_name','brand_name','remarks','member','site','floor','date_from','date_to', 'division']


class ItemBaseFilter(django_filters.FilterSet):
    site = ChoiceFilter(field_name='site', label="SITE", choices=site_list)
    item_name = CharFilter(field_name='item_name', lookup_expr='icontains', label="ITEM NAME")
    brand_name = CharFilter(field_name='brand_name', lookup_expr='icontains', label="BRAND NAME")
    date_from = DateFilter(field_name='date_added', lookup_expr='date__gte', label="DATE FROM", widget=DateInput(attrs={'type': 'date'}))
    date_to = DateFilter(field_name='date_added', lookup_expr='date__lte', label="DATE TO", widget=DateInput(attrs={'type': 'date'}))
    demand_item = ChoiceFilter(field_name='demand_item', label="DEMAND ITEM", choices=demand_item_list)
    division = ChoiceFilter(field_name='division', label="DIVISION", choices=division_list)

    class Meta:
        model = ItemBase
        fields = ['site','item_name','brand_name','date_from','date_to','demand_item','division']
