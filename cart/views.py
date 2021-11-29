from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
global name
def cart_details(request,count=0,ct_items=None,tot=0):
   if 'username' in request.session:
       try:
            ct=cartlist.objects.get(username=usename(request))
            ct_items=items.objects.filter(cart_id=ct,active=True)
            for i in ct_items:
                tot +=(i.prodt.price*i.quantity)
                count+=i.quantity
                print(count)
       except ObjectDoesNotExist:
           pass
       return render(request,'cart.html',{'ci':ct_items,'tot':tot,'cn':count})
   else:
       return redirect('login')
def c_id(request):
    ct_id=request.session.session_key
    return ct_id
def usename(request):
    for KEY in request.session.keys():
         name = request.session[KEY]
         print(1,name)
    return name

def add_cart(request,product_id):
    prod=products.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(username=usename(request))
        print(ct)
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request),username=usename(request))
        ct.save()
    try:
        c_items=items.objects.get(prodt=prod,cart=ct)
        if c_items.quantity < c_items.prodt.stock:
            c_items.quantity+=1
            c_items.price=c_items.quantity * c_items.prodt.price
            c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prodt=prod,quantity=1,cart=ct)
        c_items.price = c_items.quantity * c_items.prodt.price
        c_items.save()
    return redirect('CartDetails')




def min_cart(request,product_id):

    ct=cartlist.objects.get(username=usename(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prodt=prod,cart_id=ct)
    if c_items.quantity>1:
        c_items.quantity-=1
        c_items.price = c_items.quantity * c_items.prodt.price
        c_items.save()
    else:
        c_items.delete()
    return redirect('CartDetails')

def cart_delete(request,product_id):
    ct = cartlist.objects.get(username=usename(request))
    prod = get_object_or_404(products, id=product_id)
    c_items = items.objects.get(prodt=prod, cart_id=ct)
    c_items.delete()
    return redirect('CartDetails')
