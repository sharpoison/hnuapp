# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from .models import classstatus,otsteam,building

def home(request):
# UsePer = classstatus.objects.filter(ClassStatus=1).count() / classstatus.objects.all().count()
    isum = classstatus.objects.filter(ClassStatus=1).count() / classstatus.objects.all().count()
    isum = round(isum * 100)
    isum100 = 100-isum
    ibuilding = building.objects.all().filter(id=1).first()

# UsePer = round(UsePer*100)
# Ccount = classstatus.objects.count()
#    print(isum)
#    print(isum100)
#    print(otsteam.objects.all().count())
    print(ibuilding.Name)
#    Ccontext=context({'Cstatus':classstatus.objects.all(),
#                    'Ccount1':classstatus.objects.filter(ClassStatus=1).count(),
#                    'CcountSum':classstatus.objects.all().count(),
#                    'isum':isum,
#                    'isum100':isum100,
 #                   'otsteams':otsteam.objects.all()
 #                   })

    return render(request,'index.html',context={'Cstatus':classstatus.objects.all().order_by("ClassName"),'Ccount1':classstatus.objects.filter(ClassStatus=1).count(),'CcountSum':classstatus.objects.all().count(),'isum':isum,'isum100':isum100,'otsteams':otsteam.objects.all()})

def classinfo(request):
    return render(request,'class_info.html',context={'tijiaostatus':classstatus.objects.all().order_by("ClassName").filter(Building="梯教"),'erjiaostatus':classstatus.objects.all().order_by("ClassName").filter(Building="二教"),'shuijiaostatus':classstatus.objects.all().order_by("ClassName").filter(Building="水教")})

def query_table_otsteam(request):
    return render(request,'query_table_otsteam.html',context={'otsteams':otsteam.objects.all()})

def building_gallery(request):
    return render(request,'building_gallery.html',context={'otsteams':otsteam.objects.all()})

def form_ots(request,ids):
    return render(request,'form_ots.html',context={'buildings':building.objects.all(),'ids':ids,'Cstatus':classstatus.objects.all().order_by("ClassName"),'buildings1':building.objects.all().filter(id=ids).first()})



