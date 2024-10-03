from django.contrib import admin
from .models import Item, ItemBase, ItemCode, UOM, Department, Client, TeamMember, Site, Floor

admin.site.site_header = "S360 Inventory System"

admin.site.register(Item)
admin.site.register(ItemBase)
admin.site.register(ItemCode)
admin.site.register(UOM)
# admin.site.register(Department)
# admin.site.register(Client)
admin.site.register(TeamMember)
admin.site.register(Site)
admin.site.register(Floor)


