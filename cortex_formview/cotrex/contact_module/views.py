from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import contactusModelform
from .models import contactus
from django.views import View
from django.views.generic.edit import  FormView





class contactview(FormView):
    template_name="contact_module/contact_page.html"
    form_class=contactusModelform
    success_url= "/"
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
        
        
















 
 
 
 

