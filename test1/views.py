# -*- coding: utf-8 -*-
import datetime,time
from django.utils.timezone import now,timedelta
from django.http import HttpResponse
from django.shortcuts import render
from .models import classstatus,otsteam,building,eventtype,troubleevent,week,classtime

def get_week_day(date):
  week_day_dict = {
    0 : '一',
    1 : '二',
    2 : '三',
    3 : '四',
    4 : '五',
    5 : '六',
    6 : '七',
  }
  return week_day_dict[date]

def home(request):
# UsePer = classstatus.objects.filter(ClassStatus=1).count() / classstatus.objects.all().count()
    isum = classstatus.objects.filter(ClassStatus=1).count() / classstatus.objects.all().count()
    isum = round(isum * 100)
    isum100 = 100-isum
    ibuilding = building.objects.all().filter(id=1).first()
    week_id = week.objects.all()

#    date0 = datetime.datetime.strptime(detester,'%Y.%m.%d').date()
#    idate = datetime.datetime.now().date()
#    date_1=(idate - date0).days

    for fooo in week_id:
#        print(datetime.datetime.strptime(fooo.Tdate,'%Y.%m.%d').date()-datetime.datetime.now().date())
        if datetime.timedelta(days=7)>datetime.datetime.strptime(fooo.Tdate,'%Y.%m.%d').date()-datetime.datetime.now().date()>=datetime.timedelta(days=0):
            week_id_now = fooo.weekid
            day_Week = datetime.datetime.now().weekday()
            a=get_week_day(day_Week)
            print(week_id_now)
            print(a)

    for foooo in classtime.objects.all():
        if datetime.datetime.strptime(foooo.StartTime,'%H%M').time()<datetime.datetime.now().time()<datetime.datetime.strptime(foooo.StopTime,'%H%M').time():
            Jieci_now = foooo.JieCi
            print(foooo.JieCi)
            print(Jieci_now)
            print(datetime.datetime.now().time())

# UsePer = round(UsePer*100)
# Ccount = classstatus.objects.count()
#    print(isum)
#    print(isum100)
#    print(otsteam.objects.all().count())
#    print(date0)
#    print(idate)
#    print(date_1)
#    print(week_id_now)
#    Ccontext=context({'Cstatus':classstatus.objects.all(),
#                    'Ccount1':classstatus.objects.filter(ClassStatus=1).count(),
#                    'CcountSum':classstatus.objects.all().count(),
#                    'isum':isum,
#                    'isum100':isum100,
 #                   'otsteams':otsteam.objects.all()
 #                   })

    return render(request,'index.html',context={'Cstatus':classstatus.objects.all().order_by("ClassName"),'Ccount1':classstatus.objects.filter(ClassStatus=1).count(),'CcountSum':classstatus.objects.all().count(),'isum':isum,'isum100':isum100,'otsteams':otsteam.objects.all(),'troubleevents1':troubleevent.objects.all()[:6]})

def classinfo(request):
    return render(request,'class_info.html',context={'tijiaostatus':classstatus.objects.all().order_by("ClassName").filter(Building="梯教"),'erjiaostatus':classstatus.objects.all().order_by("ClassName").filter(Building="二教"),'shuijiaostatus':classstatus.objects.all().order_by("ClassName").filter(Building="水教"),'tijiaostatus_on':classstatus.objects.all().order_by("ClassName").filter(Building="梯教",ClassStatus=1)})

def query_table_otsteam(request):
    return render(request,'query_table_otsteam.html',context={'otsteams':otsteam.objects.all()})

def building_gallery(request):
    return render(request,'building_gallery.html',context={'otsteams':otsteam.objects.all()})

def form_ots(request,ids):
    return render(request,'form_ots.html',context={'buildings':building.objects.all(),'ids':ids,'Cstatus':classstatus.objects.all().order_by("ClassName"),'buildings1':building.objects.all().filter(id=ids).first(),'eventtypes':eventtype.objects.all(),'otsteams':otsteam.objects.all()})

def query_event(request):
    return render(request,'query_table_event.html',context={'troubleevents':troubleevent.objects.all()})

