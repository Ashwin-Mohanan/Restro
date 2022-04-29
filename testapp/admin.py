from django.contrib import admin
from testapp.models import Restro
# Register your models here.
class RestroAdmin(admin.ModelAdmin):
    list_display=['Name','Taste','Price']
admin.site.register(Restro,RestroAdmin)

# class Non_VegAdmin(admin.ModelAdmin):
#     list_display=['NV_Name','NV_Taste','NV_Price']
# admin.site.register(Non_Veg,Non_VegAdmin)

# class VegAdmin(admin.ModelAdmin):
#     list_display=['vname','vtaste','vprice']
# admin.site.register(Veg,VegAdmin)
