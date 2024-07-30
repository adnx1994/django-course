from . import urls
from django.http import HttpResponse






# تابع های نمایش دهنده در پزوژه اصلی


def index(request):
    return HttpResponse("main index page")
