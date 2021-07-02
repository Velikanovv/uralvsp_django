from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
import random
from django.contrib.auth.hashers import make_password
from django.utils import timezone
import datetime as DT
from decimal import Decimal
from news.models import *

def news(request):
    if request.method == 'GET':
        news = News.objects.all().order_by('-date')
        return render(request, 'news/news.html', {'news': news })

def news_detail(request, pk):
    if request.method == 'GET':
        new = News.objects.filter(pk=pk).first()
        return render(request, 'news/news_detail.html', {'new': new })