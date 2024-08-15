from django import forms


class searcherForm(forms.Form):
    
    searcher=forms.CharField(label='',widget=forms.TextInput(attrs={ 'class' :'sabt-input'  ,'placeholder': "جستجوی نماد مورد نظر"    }  )  )