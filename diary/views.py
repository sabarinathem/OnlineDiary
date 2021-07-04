from django.db.models.fields import DateField, DateTimeField
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from diary.models import Diary
from diary.form import DiaryForm
import datetime

def index(request):
    diary=Diary.objects.order_by('-id')
    context={'diary':diary}
    return render(request,'diary/index.html',context)
def add(request):
    if request.method=='POST':
        df=DiaryForm(request.POST)
        if df.is_valid():
            df.save()   
            return redirect('index') 
    else:
        df=DiaryForm()
    context={'form':df}
    return render(request,'diary/add.html',context)
def main(request):
    return render(request,'diary/main.html')
def diary(request,id):
    diary=Diary.objects.get(pk=id)
    context={'diary':diary}
    return render(request,'diary/diary.html',context)
def edit(request,id):
    if request.method=="POST":
        text=request.POST['diary']
        diary=Diary.objects.get(pk=id)
        diary.text=text
        diary.date=datetime.datetime.now()
        # d=datetime.datetime.now()
        # diary.date.Date=d.date()
        # diary.date.Time=d.strftime("%I:%M:%S")

        diary.save()
        return redirect('index')
  
    diary=Diary.objects.get(pk=id)
   
    context={'diary':diary}
    return render(request,'diary/edit.html',context)

def delete(request,id):
    diary=Diary.objects.get(pk=id)
    diary.delete()
    return redirect('index')

