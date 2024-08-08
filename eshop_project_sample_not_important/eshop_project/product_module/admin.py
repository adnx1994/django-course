from django.contrib import admin
from . import models

# Register your models here.




class productAdmin(admin.ModelAdmin):
    prepopulated_fields={
        'slug' : ['title']
    }


    list_display=['__str__','price','rating','is_active','category','information',]
    
    list_filter=['rating','is_active']
    
    list_editable=['rating','category','information']




#########


class productcategoryAdmin(admin.ModelAdmin):
    
    list_display=['__str__','title','url_title']






class  productinformationAdmin(admin.ModelAdmin):

    list_display=['__str__','color','size']






class  producttagAdmin(admin.ModelAdmin):

    list_display=['__str__','tag']





#######

admin.site.register(models.product ,productAdmin)
admin.site.register(models.productcategory,productcategoryAdmin)
admin.site.register(models.productinformation,productinformationAdmin)
admin.site.register(models.producttags,producttagAdmin)