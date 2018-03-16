from django.db import models

# Create your models here.
class classstatus(models.Model):
    ClassName = models.CharField(max_length=50)
    Building = models.CharField(max_length=50)
    ClassStatus = models.IntegerField()
    UpdateTime = models.DateTimeField()


