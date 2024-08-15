from django.contrib import admin
from . import models
# Register your models here.







class contactusAdmin(admin.ModelAdmin):


    list_display=['__str__','username','email','subject','is_read_by_admin','created_date']
    
    list_filter=['username','email','is_read_by_admin']
    






admin.site.register(models.contactus,contactusAdmin)