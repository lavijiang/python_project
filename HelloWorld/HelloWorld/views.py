from django.http import HttpResponse
from django.shortcuts import render

def runoob(request):
    context          = {}
    context['hello'] = 'Hello World! this is lavijiang'
    return render(request, 'runoob.html', context)


def runoob2(request):
    views_name = "θιΈζη¨"
    return  render(request,"runoob2.html", {"name":views_name})

def hello(request):
    return render(request, 'index.html')

def game(request):
    return render(request, 'game.html')