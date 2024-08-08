from django.shortcuts import render
from .models import product,productcategory
from django.http import Http404
from django.db.models import Avg

# Create your views here.


def product_list(request):
    products = product.objects.all()
    number_of_products=products.count()
    average_rating=products.aggregate(Avg("rating"))
    

    
    
    
    context = {
        "products": products,
        "total_number_of_products" :number_of_products,
        "average_rating" :average_rating,

    }
    return render(request, "product_module/product_list.html", context)







def product_detail(request, slug):

    try:
        productex = product.objects.get(slug=slug)

        
         
    except:
        raise Http404()



    context = {
        "product": productex,

    }

    return render(request, "product_module/product_detail.html", context)
