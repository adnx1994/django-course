from django.db import models

# Create your models here.




class contactus(models.Model):
    username=models.CharField(max_length=300 , verbose_name="نام کاربری")
    email=models.EmailField( verbose_name="ایمیل")
    subject=models.CharField(max_length=200 , verbose_name=" موضوع")
    comment=models.CharField(max_length=300 , verbose_name="متن نظر")
    created_date=models.DateTimeField(max_length=300 , verbose_name="تاریخ ایجاد",auto_now_add=True)
    response=models.TextField(max_length=300 , verbose_name="پاسخ ادمین",null=True,blank=True)
    is_read_by_admin=models.BooleanField(verbose_name="خوانده شده توسط ادمین")
    
    class Meta:
        verbose_name="تماس با ما"
        verbose_name_plural="لیست تماس با ما"
        
        
    def __str__(self) :
        return self.username