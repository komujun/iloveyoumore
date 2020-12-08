from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Mypage(models.Model):
    user_name = models.CharField(max_length=40,null=False)
    p1 = models.CharField(max_length=40,null=True)
    p2 = models.CharField(max_length=40,null=True)
    relationship = models.CharField(max_length=20,null=True)
    image_path = models.CharField(max_length=150,null=False)
    regi_date = models.DateTimeField(auto_now_add=True)






class Usergroup(models.Model):
    eng_name = models.CharField(max_length=100, null=False)
    kor_name = models.CharField(max_length=100,null=False)
    regi_date = models.DateTimeField(auto_now_add=True)
    pin = models.CharField(max_length=12,null=False)
    
class Access(models.Model):
    user_pk = models.ForeignKey(Usergroup,on_delete=models.CASCADE)
    enter_at = models.DateTimeField(default=datetime.datetime.now())
    out_at = models.DateTimeField(null=True,blank=True)
    recent = models.DateTimeField(default=datetime.datetime.now())


