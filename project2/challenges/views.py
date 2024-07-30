from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect,Http404
from django.urls import reverse

# Create your views here.


days = {
    "saturday": "this is saturday",
    "sunday": "this is sunday",
    "monday": "this is monday",
    "tuesday": "this is tuesday",
    "wednesday": "this is wednesday",
    "thursday": "this is thursday",
    "friday": "this is friday",
}





def days_list(request):
    days_list = list(days.keys())
    context={
        "days_list":days_list,
    }
    

    return render(request,"challenges/index.html",context)







def dynamtc_days_by_number(request, day):
    days_name = list(days.keys())
    if day > len(days_name):
        raise Http404()
    else:
        days_data_by_number = days_name[day-1]
        redirect_url=reverse("days-of-week",args=[days_data_by_number])

        return HttpResponseRedirect(redirect_url)






def dynamic_days(request, day):
    days_data = days.get(day)

    if days_data != None:
        
        context={
            "day":day,
            "days_data":days_data,
        }
        return render(request,"challenges/challenges.html",context)
    else:
        return HttpResponseNotFound("<h1 style='background-color: red;'>page is not found</h1>")
