from django.db import connection, models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.signals import post_save
import datetime
from io import BytesIO
from PIL import Image
from django.core.files import File






class Employee(models.Model):
    connection=models.OneToOneField(to=User,on_delete=CASCADE,null=True,blank=True)
    emp_name = models.CharField(max_length=30)
    emp_last_name = models.CharField(max_length=30)
    emp_gender = models.CharField(max_length=30)
    emp_dob = models.DateField()
    emp_education = models.CharField(max_length=30)
    emp_email = models.CharField(max_length=30)
    emp_field = models.CharField(max_length=30)
    emp_payment = models.CharField(max_length=30)
    emp_phone = models.CharField(max_length=30)
    emp_address = models.CharField(max_length=30)
    emp_photo = models.ImageField(upload_to='employee_photoes',blank=True,null=True)




    def __str__(self):
        return f'{self.emp_name} {self.emp_last_name}'


class Fields(models.Model):
    field_name = models.CharField(max_length=30)
    explain_field = models.TextField(blank=True,null=True)



    def __str__(self):
        return self.field_name


class Pay_slip(models.Model):
    emp_id = models.IntegerField(blank=True,null=True)
    emp_name = models.CharField(max_length=20,blank=True)
    pay_date = models.DateField(auto_now_add=True)
    basic_salary = models.IntegerField(blank=True,null=True)
    HRA = models.IntegerField(blank=True,null=True)
    other_allow= models.IntegerField(blank=True,null=True)
    total_earninig= models.IntegerField(blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True)
    amount = models.CharField(max_length=10,blank=True,null=True)
    email = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.emp_name



class Expenses(models.Model):
    amount = models.IntegerField()
    pay_to = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    Phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    describe_payment = models.TextField()


    def __str__(self):
        return self.pay_to


class Notice(models.Model):
    title= models.CharField(max_length=50)
    detail  = models.CharField(max_length=300)
    posted_by = models.CharField(max_length=50)
    date = models.DateField()


    def __str__(self):
        return self.title


class Attendance(models.Model):
    emp_iid = models.CharField(max_length=30)
    date = models.DateField()
    presenty = models.CharField(max_length=30)


    def __str__(self):
        return self.emp_iid




class Employee_personal_info(models.Model):
    emp = models.OneToOneField(to=Employee,on_delete=models.CASCADE)
    tel = models.CharField(max_length=20,blank=True,null=True)
    nationality =  models.CharField(max_length=20,blank=True,null=True)
    religion =  models.CharField(max_length=20,blank=True,null=True)
    marital_status =  models.CharField(max_length=20,blank=True,null=True)
    photo = models.FileField(upload_to='emp_photo',blank=True,null=True)





class Employee_bank_info(models.Model):
    emp = models.OneToOneField(to=Employee,on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=20,blank=True,null=True)
    bank_ac_no = models.CharField(max_length=20,blank=True,null=True)
    ifsc = models.CharField(max_length=20,blank=True,null=True)
    pan = models.CharField(max_length=20,blank=True,null=True)












