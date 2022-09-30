from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# user register.
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

# user login. 
def user_login(r):
    if r.method == "GET":
        return render(r,"6/user_login.html")
    if r.method == "POST":
        uname = r.POST.get('username','')
        pwd = r.POST.get('password','')
        if User.objects.filter(username=uname):
            user = authenticate(username=uname,password=pwd)
            if user:
                if user.is_active:
                    login(r,user)
                    info = "登录成功"
                else:
                    info = "用户还未激活"
            else:
                info = "账号密码错误，请重新输入"
        else:
            info = "用户账户不存在，请查询"           
        return render(r,"6/user_login.html",{"info":info})