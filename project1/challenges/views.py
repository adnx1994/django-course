from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse



#تابع های نمایش دهنده در ماژول challenges






def xxchallenges(request):
    return HttpResponse("صفحه اصلی challenges هستید sunday  یا monday را بنویسید")





def saturday(request):
    return HttpResponse("this is saturday")




def sunday(request):
    return HttpResponse("this is sunday")