from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def user_reg(r):
    if r.method == "GET":
        return render(r,"6/user_reg.html")
    if r.method == "POST":
        uname = r.POST.get('username','')
        pwd = r.POST.get('password','')
        if User.objects.filter(username=uname):
            info="用户已经存在"
        else:
            d=dict(username=uname,password=pwd,email='111@111.com',is_staff=1,is_active=1,is_superuser=1)
            user=User.objects.create_user(**d)
            info="注册成功，请登录"
        return render(r,"6/user_reg.html",{"info":info})
    
