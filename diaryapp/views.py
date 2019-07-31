from django.shortcuts import render, redirect
from .models import Diary
from django.utils import timezone

# Create your views here.

def home(request):
    diarys=Diary.objects
    return render(request, 'home.html',{'diarys': diarys})

def new(request):
    return render(request,'new.html')

def create(request):
    diary=Diary()
    diary.title=request.GET['title']
    diary.body=request.GET['body']
    diary.pub_date=timezone.datetime.now()
    diary.save()
    return redirect('home')