from django.shortcuts import render

def index(request):
     return render(request, 'index/index.html')

def auth(request):
     return render(request, 'main/Authorization.html')

def about(request):
     return render(request, 'main/about.html')

