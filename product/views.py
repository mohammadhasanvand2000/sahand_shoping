from django.http import HttpResponseRedirect,HttpResponse
from itertools import product
from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.urls import reverse

from .models import Product,Client_Coments,Cart,Product_image,Detail,Product_color,Grouping
from .forms import Cart_Form 
from django.db.models import Avg, Sum, Max, Min ,Count

def index (request):
    
    return render (request,'product/index.html')


class ProductsListView(generic.ListView):
    
    model=Product
    paginate_by =8





def detailproduct(request,id):

    if request.method =="GET":
        detail = Detail.objects.filter(id=id)
        image =Product_image.objects.filter(producti__id__exact=id)
        product=Product.objects.filter(id=id)
        color=Product_color.objects.filter(producti__id__exact=id)
        context={'detail':detail,'image':image,'product':product,'color':color}

        return render(request,'product/detail_detail.html',context)



def grouping(request):

    if request.method =="GET":
        group    = Grouping.objects.all()
        #product  = Product.objects.filter(grouping__id__exact=id)

        context={'group':group}
        return render(request,'product/grouping_heder_list.html',context)







def gproduct(request,id):

    if request.method =="GET":
        product_list  = Product.objects.filter(grouping__id__exact=id)

        context={'product_list':product_list}
        return render(request,'product/grouping_list.html',context)

        

def add_cart(request,id):
    
    if request.method =="GET":
        buy =Cart.objects.create(product_id=id , buy_from_avalable=1)
         
        return render(request, 'product/detail_detail.html', {'buy': buy})





def cart(request):

    if request.method =="GET":
        f=Cart.objects.all() 
        d=Cart.objects.aggregate(Count('product'))
        c=d['product__count'] 
        a=Cart.objects.values_list('product__price', flat=True)  
        s=sum(a)
         
                
        return render(request, 'product/cart.html', {'f': f,'c': c,'s': s}) 





def delete_cart (request,id):

    data = Cart.objects.filter(product__id=id) 
    data.delete()
    return render(request,'product/cart.html',{}) 




    
    