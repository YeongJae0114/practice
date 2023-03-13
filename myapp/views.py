from django.shortcuts import render, redirect
from .models import cmodel
from .forms import cform

def home(request):
    return render(request, 'home.html')

def new(request):
    return render(request, 'new.html')

    

def createmf(request):
    if request.method =='POST':
        form = cform(request.POST)
        if form.is_valid(): #데이터 유효성 검사
            form.save()
            return redirect('home')
    else:
        form = cform()
    return render(request, 'new.html', {'form':form})    