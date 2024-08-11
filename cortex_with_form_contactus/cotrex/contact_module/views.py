from django.shortcuts import render

# Create your views here.



def contact(request):
    if request.method=="POST" :
        print(request.POST)
        print(request.POST['username'])
        print(request.POST['email'])
    return render(request,"contact_module/contact_page.html")