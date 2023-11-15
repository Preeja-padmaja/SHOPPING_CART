from django.shortcuts import render
from Shopping_Cart_App.models import product_table
from django.db.models import Q
# Create your views here.
def search_result(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=product_table.objects.all().filter(Q(p_name__contains=query) | Q(desc__contains=query))
    return render(request,'search.html',{'query':query,'products':products})

