from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import contactusModelform
from .models import contactus



def contact(request):
    if request.method=='POST' :
            contact_form= contactusModelform(request.POST)
            if contact_form.is_valid():
                print(contact_form.cleaned_data)

                contact_form.save()
                return redirect(reverse('main'))
                 
    else:
        contact_form= contactusModelform()
    return render(request,"contact_module/contact_page.html",{
        'contact_form' :contact_form,

    })
 
 
 
 
 
 

