from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page= get_object_or_404(category,slug=c_slug)
        prodt=products.objects.filter(categary=c_page,available=True)
    else:
        prodt=products.objects.all().filter(available=True)
    cat=category.objects.all()

    p=Paginator(prodt,4)
    page_num=request.GET.get('page',1)
    try:
        page=p.page(page_num)
    except (InvalidPage,EmptyPage) as e:
        raise e
        page=p.page(1)

    return render(request,'home.html',{'pr':prodt,'ct':cat,'pg':page})

def proddetails(request,c_slug,prod_slug):
    try:
        prod=products.objects.get(categary__slug=c_slug,slug=prod_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'pr':prod})
def search(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        print(query)
        prod=products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))

    return render(request,'search.html',{'qr':query,'pr':prod})