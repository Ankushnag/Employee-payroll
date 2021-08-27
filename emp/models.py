from django.db import connection, models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
import datetime
from io import BytesIO
from PIL import Image
from django.core.files import File

# Create your models here.


class tasks(models.Model):
    emp_con =models.ForeignKey(to=User,on_delete=CASCADE,null=True,blank=True)
    task_name = models.CharField(max_length=10,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    start_date=models.DateField(null=True, blank=True)
    end_date=models.DateField(null=True, blank=True)
    status=models.CharField(default='Pending',max_length=10)

class leaves(models.Model):
    emp_con =models.ForeignKey(to=User,on_delete=CASCADE,null=True,blank=True)
    leave_type=models.CharField(max_length=20,null=True,blank=True)
    from_date =models.CharField(max_length=20,null=True,blank=True)
    to_date=models.CharField(max_length=20,null=True,blank=True)
    reson=models.CharField(max_length=50,null=True,blank=True)
    Status=models.CharField(max_length=10,null=True,blank=True)

class project(models.Model):
    
    project_title=models.CharField(max_length=20,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    Deadline=models.DateField(null=True,blank=True)
    status = models.CharField(max_length=10,null=True,blank=True)





