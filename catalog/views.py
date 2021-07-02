from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
import random
from django.contrib.auth.hashers import make_password
from django.utils import timezone
import datetime as DT
from decimal import Decimal
from catalog.models import *


def new_list_columns(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def production(request):
    if request.method == 'GET':
        production = Production.objects.all()
        return render(request, 'catalog/production.html', {'production': production })

def service(request):
    if request.method == 'GET':
        service = Service.objects.all()
        return render(request, 'catalog/service.html', {'service': service })

def category(request):
    if request.method == 'GET':
        cats = Category.objects.all()
        return render(request, 'catalog/category.html', {'cats': cats })

def subcategory(request, pk):
    if request.method == 'GET':
        cat = Category.objects.filter(pk=pk).first()
        subcats = SubCategory.objects.filter(category=cat).all()
        return render(request, 'catalog/subcategory.html', {'cat': cat, 'subcats': subcats })

def product_list(request, pk, s_pk):
    if request.method == 'GET':
        cat = Category.objects.filter(pk=pk).first()
        subcat = SubCategory.objects.filter(pk=s_pk).first()
        products = Product.objects.filter(subcategory=subcat)
        return render(request, 'catalog/product_list.html', {'cat': cat, 'subcat': subcat,'products': products })

def product(request, pk, s_pk, p_pk):
    if request.method == 'GET':
        cat = Category.objects.filter(pk=pk).first()
        subcat = SubCategory.objects.filter(pk=s_pk).first()
        product = Product.objects.filter(pk=p_pk).first()
        subproducts = SubProduct.objects.filter(product=product).all()
        sub_relist = new_list_columns(subproducts, 4)
        productparams = ProductParam.objects.filter(product=product).all()
        productvalues = ProductValue.objects.filter(product=product).all()
        return render(request, 'catalog/product.html', {'cat': cat, 'subcat': subcat,'product': product,'subproducts':subproducts, 'productparams': productparams,'productvalues': productvalues, 'sub_relist': sub_relist,'len_sr':len(sub_relist) })
    if request.method == 'POST':
        product = Product.objects.filter(pk=p_pk).first()
        productvalues = ProductValue.objects.filter(product=product).all()
        for value in productvalues:
            value.title = request.POST[str(value.pk)]
            value.save()
        return redirect('product',pk,s_pk,p_pk)