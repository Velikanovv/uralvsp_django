from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('politics/', views.politics, name='politics'),
    path('contacts/', views.contacts, name='contacts'),
    path('feedback/', views.feedback_post, name='feedback'),
    path('application/', views.application_post, name='application'),
    path('p/<slug:page_s>/', views.page, name='page')
]
