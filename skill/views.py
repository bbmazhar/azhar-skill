from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def skill1(request):
    return render(request, 'skill1.html')

def skill2(request):
    return render(request, 'skill2.html')

def skill3(request):
    return render(request, 'skill3.html')