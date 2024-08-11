from django.shortcuts import render
from django.http import Http404






def index(request):
   if  (request.method=="POST"):
          print(request.POST["searcher"])
          
   return render(request,"index.html")





