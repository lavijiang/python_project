from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import os
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def upload_file(r):
    if r.method == "GET":
        return render(r,"5/upload.html")
    if r.method == "POST":
        myFile = r.FILES.get("myfile",None)
        if myFile:
            path='media/uploads'
            if not os.path.exists(path):
                os.makedirs(path)
            dest = open(os.path.join(path, myFile.name),'wb+')
            for chunk in myFile.chunks():
                dest.write(chunk)
                dest.close()
            return HttpResponse("上传完成!")
        else:
            return HttpResponse("没有上传文件!")
    
#@csrf_exempt        
def  ajax_login(r):
    return render(r,"5/ajax.html")
#@csrf_exempt  
def  ajax_login_data(r):
    username = r.POST.get("username")
    password = r.POST.get("password")
    if username == 'admin' and password == "123456":
        return JsonResponse({'code':0,"msg":"success"})
    else:
        return JsonResponse({'code':-1,"msg":"fail"})