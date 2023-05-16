"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

import app1
import djangoProject1
from djangoProject1 import views

# from django.conf.urls import handler404, handler500
urlpatterns = [
    path('admin/', admin.site.urls),
    path('page1_view', views.page1_view),
    # http://127.0.0.1:8000/page2_view/王冠一   ----路由变量
    path('page2_view/<str:name>', views.page2_view),

    # mypage?a=100&b=200&c=300&d=400
    path('mypage', views.mypage),
    # /test_html01
    path('test_html01', views.test_html01,name='test_html'),
    # /test_html011
    path('test_html02', views.test_html02,name='name'),
    path('test_html_param', views.test_html_param,name='test_html_param'),

    # /mycal 计算器--练习
    path('mycal',views.mycal),

    path('test_url_result',views.test_url_result,name='ur'),
]
