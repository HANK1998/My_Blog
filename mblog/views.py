from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
    articals = models.Artical.objects.all()
    return render(request,'index.html',{'articals':articals})

def artical_page(request,artical_id):
    artical = models.Artical.objects.get(pk=artical_id)
    return render(request,'artical_page.html',{'artical':artical})

def artical_edit_page(request):
    return render(request,'artical_edit_page.html')

def artical_edit_page_action(request):
    title = request.POST.get('title','默认标题')
    content = request.POST.get('content','默认内容')
    models.Artical.objects.create(title=title,content=content)
    articals = models.Artical.objects.all()
    return render(request,'index.html',{'articals':articals})