# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template import Context

from torske.members.models import Member

def index(request):
    # View code here...
    return render(request, 'index.html')
    
def info(request):
    return render(request, 'info.html')
    
def news(request):
    return render(request, 'news.html')
    
def programs(request):
    return render(request, 'programs.html')
    
def photos(request):
    return render(request, 'photos.html')
    
def login(request):
    return render(request, 'login.html')
    
def directory(request):
    return render(request, 'directory.html')
    
def students(request):
    return render(request, 'students.html')
    
def members(request):
    all_members = Member.objects.all()
    return render(request, 'members.html', 
                  context=Context({'members': all_members}))
    
    
    
    
    
    
    
    