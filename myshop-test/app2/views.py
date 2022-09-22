from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("app2的index方法")

def show(request,id):
    return HttpResponse("app2的show方法，参数为id，值为"+str(id))

def test_get(request):
    print(request.get_host())
    print(request.build_absolute_uri())
    print(request.path)
    print(request.get_full_path())
    print(request.method)
    print(request.GET)
    print(request.META["HTTP_USER_AGENT"])
    print(request.META["REMOTE_ADDR"])
    print(request.GET.get('username'))
    return HttpResponse("")

def test_post(request):
    print(request.method)
    print(request.POST.get('username'))
    return render(request,'2/test_post.html')

def test_render(request):
    return render(request,'2/test_render.html',{'info':'hello django'},content_type='text/html')