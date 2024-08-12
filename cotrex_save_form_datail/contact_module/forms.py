from django import forms


class contactusForm(forms.Form):
    
    username=forms.CharField(label='',widget=forms.TextInput(attrs={ 'class' :'nazar_user'  ,'placeholder': "نام کاربری"    }  )  )
    email=forms.EmailField(label='',widget=forms.EmailInput(attrs={ 'class' :'nazar_user'  ,'placeholder': "ایمیل"    }  ))
    subject=forms.CharField(label='',widget=forms.TextInput(attrs={ 'class' :'nazar_user'  ,'placeholder': "موضوع"    }  ) )
    comment=forms.CharField(label='',widget=forms.Textarea(attrs={ 'class' :'nazar_user'  ,'placeholder': "متن مورد نظر"    }  ))