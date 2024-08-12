from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import contactusForm
from .models import contactus






def contact(request):
    if request.method=='POST' :
            contact_form= contactusForm(request.POST)
            if contact_form.is_valid():
                print(contact_form.cleaned_data)
                contact=contactus(
                    username=contact_form.cleaned_data.get("username"),
                    email=contact_form.cleaned_data.get("email"),
                    subject=contact_form.cleaned_data.get("subject"),
                    comment=contact_form.cleaned_data.get("comment"),
                    is_read_by_admin=False,
                )
                contact.save()
                return redirect(reverse('main'))
                 
    else:
        contact_form= contactusForm()
    return render(request,"contact_module/contact_page.html",{
        'contact_form' :contact_form,

    })
    