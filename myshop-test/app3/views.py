from django.shortcuts import render
from app3 import templatetags

# Create your views here.
def var(r):
    lists = ['Java','Python','Cpp']
    dicts = {'姓名':'张三','年龄':25}
    return render(r,'3/var.html',{'lists':lists,'dicts':dicts})

def diy_filter(r):
    dict1 = {'标题':'1222eeeeeeeeeee213d'}
    dict2 = {'标题':'1222e'}
    lists = [dict1,dict2]
    return render(r,'3/diy_filter.html',{'lists':lists})

def diy_tags(r):
    dict1 = {'标题':'1222eeeeeeeeeee213d'}
    dict2 = {'标题':'1222e'}
    lists = [dict1,dict2]
    return render(r,'3/diy_tags.html',{'lists':lists})

def welcome(r):
    return render(r,'3/welcome.html')