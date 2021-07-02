from django.urls import path

from . import views

urlpatterns = [
    path('', views.category, name='category'),
    path('<int:pk>/', views.subcategory, name='subcategory'),
    path('<int:pk>/<int:s_pk>/', views.product_list, name='product_list'),
    path('<int:pk>/<int:s_pk>/<int:p_pk>/', views.product, name='product'),
    path('production/', views.production, name='production'),
    path('service/', views.service, name='service'),
]
