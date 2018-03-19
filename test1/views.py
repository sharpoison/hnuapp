# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from .models import classstatus,otsteam

def home(request):
# UsePer = classstatus.objects.filter(ClassStatus=1).count() / classstatus.objects.all().count()
    isum = classstatus.objects.filter(ClassStatus=1).count() / classstatus.objects.all().count()
    isum = round(isum * 100)
    isum100 = 100-isum

# UsePer = round(UsePer*100)
# Ccount = classstatus.objects.count()
#    print(isum)
#    print(isum100)
#    print(otsteam.objects.all().count())
#    Ccontext=context({'Cstatus':classstatus.objects.all(),
#                    'Ccount1':classstatus.objects.filter(ClassStatus=1).count(),
#                    'CcountSum':classstatus.objects.all().count(),
#                    'isum':isum,
#                    'isum100':isum100,
 #                   'otsteams':otsteam.objects.all()
 #                   })

    return render(request,'index.html',context={'Cstatus':classstatus.objects.all(),'Ccount1':classstatus.objects.filter(ClassStatus=1).count(),'CcountSum':classstatus.objects.all().count(),'isum':isum,'isum100':isum100,'otsteams':otsteam.objects.all()})

def classinfo(request):
    return render(request,'class_info.html')

