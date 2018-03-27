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








