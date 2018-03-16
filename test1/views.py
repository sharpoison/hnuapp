# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from test1.models import classstatus

def home(request):
 #   for i in classstatus.objects.all():
# Ccount = classstatus.objects.count()
 #       print(classstatus.ClassName')

    return render(request,'index.html',context={'Cstatus':classstatus.objects.all(),'Ccount1':classstatus.objects.filter(ClassStatus=1).count()})