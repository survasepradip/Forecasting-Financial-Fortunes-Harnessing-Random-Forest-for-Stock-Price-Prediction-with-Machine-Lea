from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome , name='welcome') , 
    path('home/', views.home , name='home') , 
    path('chart/', views.chart , name='chart') ,
    path('news/', views.news , name='news') ,
    path('guide/', views.guide , name='guide') ,
    path('guide/finance_guide/', views.finance , name='finance') , 
    path('guide/real_estate_guide/', views.realestate , name='realestate') ,
    path('guide/crypto_guide/', views.crypto , name='crypto') ,
    path('guide/stock_guide/', views.stock , name='stock') ,


    path('about/', views.about , name='about') ,
    path('test/', views.test , name='test') ,
]

#  path('discuss/', views.discuess , name='discuss') ,
