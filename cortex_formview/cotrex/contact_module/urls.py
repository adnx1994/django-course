from django.urls import path
from . import views



urlpatterns = [
    
    path("",views.contactview.as_view(),name="contact_us"),
    
]