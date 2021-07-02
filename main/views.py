from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
import random
from django.contrib.auth.hashers import make_password
from django.utils import timezone
import datetime as DT
from decimal import Decimal
from news.models import News
from main.models import FeedBack, Application
from settings.models import Politics, Contacts, MessageSettings, Page
from django.core.mail import send_mail

def index(request):
    if request.method == 'GET':
        news = News.objects.filter().order_by('-date')[:4]
        return render(request, 'main/index.html', {'news': news })

def politics(request):
    if request.method == 'GET':
        politics = Politics.objects.first()
        return render(request, 'main/politics.html', {'politics': politics })

def contacts(request):
    if request.method == 'GET':
        contacts = Contacts.objects.first()
        return render(request, 'main/contacts.html', {'contacts': contacts })

def feedback_post(request):
    if request.method == 'GET':
        text = request.GET.get('text')
        try:
            feed = FeedBack.objects.create(text=text)
            feed.save()
            message = MessageSettings.objects.filter().first()
            return render(request, 'main/done.html', {'message': message.feedback_done_message })
        except Exception as e:
            return render(request, 'main/error.html', {'error': e.args[0]})

def application_post(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        email = request.GET.get('email')
        number = request.GET.get('number')
        text = request.GET.get('text')
        help = request.GET.get('help')
        try:
            head = 'HEAD'
            text = 'TEST1\nTEST2\nTEST3\n'
            from_email = 'robot@uralvsp.ru'
            to_email = 'andreyvel77@gmail.com'
            send_mail(head, text, from_email, [to_email,], fail_silently=False)
            app = Application.objects.create(name=name,email=email,phone=number,text=text,help=help)
            app.save()
            message = MessageSettings.objects.filter().first()
            return render(request, 'main/done.html', {'message': message.application_done_message })
        except Exception as e:
            return render(request, 'main/error.html', {'error': e.args[0]})

def page(request, page_s):
    if request.method == 'GET':
        page = Page.objects.filter(slug=page_s).first()
        return render(request, 'main/page.html', {'c_page': page })



