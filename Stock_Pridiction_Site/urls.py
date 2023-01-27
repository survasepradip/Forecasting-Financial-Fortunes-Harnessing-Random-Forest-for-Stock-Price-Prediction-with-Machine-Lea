"""Stock_Pridiction_Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include 
from stock_site import views
from accounts import views
# from discuss import views
from discuss_part2 import views
from chat import views


urlpatterns = [
    path('', include('stock_site.urls')) ,
    path('account/', include('accounts.urls')) ,
    path('chat/', include('chat.urls')) ,
    #path('discuss/', include('discuss.urls')) ,
    path('discuss1/', include('discuss_part2.urls')) ,
    path('admin/', admin.site.urls),
    path('user_post/', views.user_post , name='user_post') ,

]
