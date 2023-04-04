"""pinterest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from accountapp.views import hello_world, AccountCreateView

# app_name 변수를 지정하는 이유는 후에 "accountapp:hello_world" 같 값을 input 으로 http://127.0.0.1:8000/account/hello_world 같은
# url 을 반환하는 함수를 쓰기 위함이다.
app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create'), # CSV를 가져와 쓸 때는 .as_view()를 해줘야한다.
]
