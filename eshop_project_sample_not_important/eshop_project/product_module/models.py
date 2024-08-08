from typing import Iterable
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


##################### هربار که چیز جدیدی را اضافه کردم و در موقع makemirgrate ارو دیدیم باید    باید   admin log ها را از دیتا بیس پاک کنیم

#################
#################
#################

# ساخت جدول دسته بندی محصولات
class productcategory(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")
    url_title = models.CharField(max_length=300, verbose_name="عنوان در url")

    def __str__(self):
        return f"{self.title}  ({self.url_title})"


#################
#################
#################


class productinformation(models.Model):
    color=models.CharField(max_length=200,verbose_name="رنگ")
    size=models.CharField(max_length=200,verbose_name="سایز")

    def __str__(self):
        return f"{self.color}-{self.size}"





#################
#################
#################

class producttags(models.Model):
    tag = models.CharField(max_length=300,verbose_name="عنوان تگ")
    

    def __str__(self):
        return f"{self.tag}"











#################
#################
#################


# ساخت جدول محصولات

class product(models.Model):
    
    title = models.CharField(max_length=300)
    
    category = models.ForeignKey(productcategory, on_delete=models.CASCADE,null=True)        # اتصال به product category  رابطه یک به چند
    information=models.OneToOneField(productinformation,on_delete=models.CASCADE,null=True,blank=True)  # رابطه یک به یک
    tags=models.ManyToManyField(producttags,)        # رابطه چند به چند
    
    
    price = models.IntegerField()
    rating = models.BigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(
        5)], default=0)        # between 1 star and 5 star for rating product
    short_description = models.CharField(max_length=360, null=True)
    is_active = models.BooleanField(default=False)
    # مثلا عنوان محصول را به لینک مفهومی تبدیل میکند
    slug = models.SlugField(default="", null=False, db_index=True)

    # db_index=True     باعث میشود سرعت دریافت دیتا ها بهتر باشد
    def get_absolute_url(self):
        return reverse("product-detail", args=[self.slug])

    def save(self, *args, **kwargs):
        # مثلا عنوان محصول را به لینک مفهومی تبدیل میکند
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"
