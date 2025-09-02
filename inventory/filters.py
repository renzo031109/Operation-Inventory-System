import django_filters
from django_filters import DateFilter, CharFilter, ChoiceFilter
from .models import Item, ItemBase, Site, Floor, TeamMember, DemandItems, Division
from django_filters import ModelChoiceFilter
from django import forms


remarks_select = (
    ('IN', 'IN'),
    ('OUT', 'OUT'),
    ('BEGINNING','BEGINNING')
)


# Unique Floor List based only on the 'floor' field
floor = Floor.objects.all()
floor_list = []
unique_floors = set()  # Track only unique floor names

for value in floor:
    normalized_floor = value.floor.strip().upper()  # Normalize by stripping spaces and converting to lowercase
    if normalized_floor not in unique_floors:
        unique_floors.add(normalized_floor)  # Add the normalized floor name to the set
        floor_list.append((value.id, value.floor))  # Append the original data to the list


class DateInput(forms.DateInput):
    input_type = 'date'


class ItemFilter(django_filters.FilterSet):
    item_name = CharFilter(field_name='item_name', lookup_expr='icontains', label="ITEM NAME")
    brand_name = CharFilter(field_name='brand_name', lookup_expr='icontains', label="BRAND NAME")
    remarks = ChoiceFilter(field_name='remarks', label="REMARKS", choices=remarks_select)
    date_from = DateFilter(field_name='date_added', lookup_expr='date__gte', label="DATE FROM", widget=DateInput(attrs={'type': 'date'}))
    date_to = DateFilter(field_name='date_added', lookup_expr='date__lte', label="DATE TO", widget=DateInput(attrs={'type': 'date'}))
    member = ModelChoiceFilter(field_name='member', label="STAFF NAME", queryset=TeamMember.objects.all())
    site = ModelChoiceFilter(field_name='site', label="SITE", queryset=Site.objects.all())
    floor = ChoiceFilter(field_name='floor', label="FLOOR", choices=floor_list)
    division = ModelChoiceFilter(field_name='division', label="DIVISION", queryset=Division.objects.all())

   
    class Meta:
        model = Item
        fields = ['item_name','brand_name','remarks','member','site','floor','date_from','date_to', 'division']


class ItemBaseFilter(django_filters.FilterSet):
    site = ModelChoiceFilter(field_name='site', label="SITE", queryset=Site.objects.all())
    item_name = CharFilter(field_name='item_name', lookup_expr='icontains', label="ITEM NAME")
    brand_name = CharFilter(field_name='brand_name', lookup_expr='icontains', label="BRAND NAME")
    date_from = DateFilter(field_name='date_added', lookup_expr='date__gte', label="DATE FROM", widget=DateInput(attrs={'type': 'date'}))
    date_to = DateFilter(field_name='date_added', lookup_expr='date__lte', label="DATE TO", widget=DateInput(attrs={'type': 'date'}))
    demand_item = ModelChoiceFilter(field_name='demand_item', label="DEMAND ITEM", queryset=DemandItems.objects.all())
    division = ModelChoiceFilter(field_name='division', label="DIVISION", queryset=Division.objects.all())

    class Meta:
        model = ItemBase
        fields = ['site','item_name','brand_name','date_from','date_to','demand_item','division']
