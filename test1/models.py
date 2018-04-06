from django.db import models

# Create your models here.
class classstatus(models.Model):
    ClassName = models.CharField(max_length=50)
    Building = models.CharField(max_length=50)
    ClassStatus = models.IntegerField()
    UpdateTime = models.DateTimeField()
    CardName = models.CharField(max_length=50,default="")

class otsteam(models.Model):
    Name = models.CharField(max_length=50)
    ImgName = models.CharField(max_length=50)
    Tel = models.CharField(max_length=50,default="")

class building(models.Model):
    Bid = models.CharField(max_length=50,default="")
    Name = models.CharField(max_length=50)
    Area = models.CharField(max_length=50)

class eventtype(models.Model):
    Name = models.CharField(max_length=50)

class troubleevent(models.Model):
    Person = models.CharField(max_length=50)
    EventClass = models.CharField(max_length=50)
    BeginDtime = models.DateTimeField()
    EndDtime = models.DateTimeField()
    EventType = models.CharField(max_length=50)
    Edescribe = models.CharField(max_length=50)
    Resolvent = models.CharField(max_length=50)

class week(models.Model):
    weekid = models.IntegerField()
    Tdate = models.CharField(max_length=50)

class classtime(models.Model):
    JieCi = models.CharField(max_length=50)
    StartTime = models.CharField(max_length=50)
    StopTime = models.CharField(max_length=50)

class course_table(models.Model):
    jgh = models.CharField(max_length=50)
    jgxm = models.CharField(max_length=50)
    Dwmc = models.CharField(max_length=200,default="")
    CardID = models.CharField(max_length=50,default="")
    Xn = models.CharField(max_length=50)
    xq = models.CharField(max_length=50)
    Zc = models.CharField(max_length=50,default="")
    Jc = models.CharField(max_length=50,default="")
    Skdd = models.CharField(max_length=200,default="")
    Skap = models.CharField(max_length=200,default="")
    Kcmc = models.CharField(max_length=100,default="")
    Bjmc = models.CharField(max_length=150,default="")
    Skbjrs = models.CharField(max_length=50,default="")











