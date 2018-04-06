# -*- coding: utf-8 -*-
import datetime,time
from django.utils.timezone import now,timedelta
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from .models import classstatus,otsteam,building,eventtype,troubleevent,week,classtime,course_table
import re

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
        if datetime.timedelta(days=7)>datetime.datetime.now().date()-datetime.datetime.strptime(fooo.Tdate,'%Y.%m.%d').date()>=datetime.timedelta(days=0):
            week_id_now = fooo.weekid
            day_Week = datetime.datetime.now().weekday()
            week_now=get_week_day(day_Week)
            print(week_id_now)
            print(week_now)

    for foooo in classtime.objects.all():
        print(datetime.datetime.now().time())
        if datetime.datetime.strptime(foooo.StartTime,'%H%M').time()<datetime.datetime.now().time()<datetime.datetime.strptime(foooo.StopTime,'%H%M').time():
            Jieci_now = foooo.JieCi
            print(foooo.JieCi)
            print(Jieci_now)
            print(datetime.datetime.now().time())
        else:
            Jieci_now = None
            print(type(Jieci_now))

#计算当前节次，周次的所有课程
    course_now = course_table.objects.all().filter(Q(Skdd__contains='中')|Q(Skdd__contains='复')|Q(Skdd__contains='综')|Q(Skdd__contains='研')|Q(Skdd__contains='前')|Q(Skdd__contains='二')|Q(Skdd__contains='水')|Q(Skdd__contains='东'),Jc=Jieci_now,Skap__contains=week_now).values('jgxm','Dwmc','Xn','xq','Zc','Skap','Skbjrs').distinct().order_by('jgxm')
#虚拟节次
    course_now1 = course_table.objects.all().filter(Q(Skdd__contains='中')|Q(Skdd__contains='复')|Q(Skdd__contains='综')|Q(Skdd__contains='研')|Q(Skdd__contains='前')|Q(Skdd__contains='二')|Q(Skdd__contains='水')|Q(Skdd__contains='东'),Jc='7-8',Skap__contains=week_now).values('jgxm','Dwmc','Xn','xq','Zc','Skap','Skbjrs').distinct().order_by('jgxm')



    print(course_now1.count(),course_now.count())
    course_count_now = 0
    course_Mem_count = 0
    for foo2 in course_now:
        reg1 = re.findall(r'(\d+)',foo2['Zc'])
        if str(week_id_now) in reg1:
            print(foo2['Zc'],reg1)
            course_count_now = course_count_now + 1
            course_Mem_count = course_Mem_count + int(foo2['Skbjrs'])
            print(week_id_now, "is here!有", course_count_now, "堂课进行中。。")
        elif '-' in foo2['Zc']:
            reg = re.compile('(\d+)(-)(\d+)')
            reg = reg.findall(foo2['Zc'])
#            print(foo2['Zc'], reg,len(reg))
#            print(foo2['Zc'],range(int(reg[0][0]),int(reg[0][2])+1))
#            print(foo2['Zc'], range(int(reg[1][0]), int(reg[1][2]) + 1))
            for foo3 in range(len(reg)):
                print(foo2['Zc'], range(int(reg[foo3][0]), int(reg[foo3][2]) + 1))
                if week_id_now in range(int(reg[foo3][0]), int(reg[foo3][2]) + 1):
                    course_count_now = course_count_now + 1
                    course_Mem_count = course_Mem_count + int(foo2['Skbjrs'])
                    print(week_id_now,"is here!有",course_count_now,"堂课进行中。。")


#    a="2,3,5,6"
#    print(eval(a))

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

    return render(request,'index.html',context={'Cstatus':classstatus.objects.all().order_by("ClassName"),'Ccount1':classstatus.objects.filter(ClassStatus=1).count(),'CcountSum':classstatus.objects.all().count(),'isum':isum,'isum100':isum100,'otsteams':otsteam.objects.all(),'troubleevents1':troubleevent.objects.all()[:6],'course_now':course_now,'course_count_now':course_count_now,'course_Mem_count':course_Mem_count})

def classinfo(request):
    return render(request,'class_info.html',context={'tijiaostatus':classstatus.objects.all().order_by("ClassName").filter(Building="梯教"),'erjiaostatus':classstatus.objects.all().order_by("ClassName").filter(Building="二教"),'shuijiaostatus':classstatus.objects.all().order_by("ClassName").filter(Building="水教"),'tijiaostatus_on':classstatus.objects.all().order_by("ClassName").filter(Building="梯教",ClassStatus=1)})

def query_table_otsteam(request):
    return render(request,'query_table_otsteam.html',context={'otsteams':otsteam.objects.all()})

def building_gallery(request):
    erjiao_room_count = classstatus.objects.filter(Building='二教').count()
    shuijiao_room_count = classstatus.objects.filter(Building='水教').count()
    tijiao_room_count = classstatus.objects.filter(Building='梯教').count()
    return render(request,'building_gallery.html',context={'otsteams':otsteam.objects.all(),'erjiao_room_count':erjiao_room_count,'shuijiao_room_count':shuijiao_room_count,'tijiao_room_count':tijiao_room_count})

def form_ots(request,ids):
    return render(request,'form_ots.html',context={'buildings':building.objects.all(),'ids':ids,'Cstatus':classstatus.objects.all().order_by("ClassName"),'buildings1':building.objects.all().filter(id=ids).first(),'eventtypes':eventtype.objects.all(),'otsteams':otsteam.objects.all()})

def query_event(request):
    return render(request,'query_table_event.html',context={'troubleevents':troubleevent.objects.all()})

def class_info_erjiao(request):
    erjiao_room_count = classstatus.objects.filter(Building='二教').count()
    shuijiao_room_count = classstatus.objects.filter(Building='水教').count()
    tijiao_room_count = classstatus.objects.filter(Building='梯教').count()
    return render(request,'class_info_erjiao.html',context={'otsteams':otsteam.objects.all(),'erjiao_room_count':erjiao_room_count,'shuijiao_room_count':shuijiao_room_count,'tijiao_room_count':tijiao_room_count})

def class_info_shuijiao(request):
    erjiao_room_count = classstatus.objects.filter(Building='二教').count()
    shuijiao_room_count = classstatus.objects.filter(Building='水教').count()
    tijiao_room_count = classstatus.objects.filter(Building='梯教').count()
    return render(request,'class_info_shuijiao.html',context={'otsteams':otsteam.objects.all(),'erjiao_room_count':erjiao_room_count,'shuijiao_room_count':shuijiao_room_count,'tijiao_room_count':tijiao_room_count})

def class_info_tijiao(request):
    erjiao_room_count = classstatus.objects.filter(Building='二教').count()
    shuijiao_room_count = classstatus.objects.filter(Building='水教').count()
    tijiao_room_count = classstatus.objects.filter(Building='梯教').count()
    return render(request,'class_info_tijiao.html',context={'otsteams':otsteam.objects.all(),'erjiao_room_count':erjiao_room_count,'shuijiao_room_count':shuijiao_room_count,'tijiao_room_count':tijiao_room_count})

