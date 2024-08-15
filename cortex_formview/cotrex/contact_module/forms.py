from django import forms
from .models import contactus


###################################




    
class contactusModelform(forms.ModelForm) :
    class Meta:
        model= contactus
        # fields=['username','email','subject','comment']     # انتخاب فیلدهای مورد نیاز
        fields= '__all__'            # انتخاب تمام 
        widgets={"username": forms.TextInput(attrs={ 'class' :'nazar_user'  ,'placeholder': "نام کاربری"    }  ),
                'email':forms.EmailInput(attrs={ 'class' :'nazar_user'  ,'placeholder': "ایمیل"    }  ),
                'subject':forms.TextInput(attrs={ 'class' :'nazar_user'  ,'placeholder': "موضوع"    }  ),
                'comment':forms.Textarea(attrs={ 'class' :'nazar_user'  ,'placeholder': "متن مورد نظر"    }  ),
                
            }
           