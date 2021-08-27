from django import http
from django.shortcuts import render, redirect,HttpResponse, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import random
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.contrib.sessions.models import Session
from datetime import date
from .models import *
import datetime
from payroll .models import *

# Create your views here.

def emp_login(request):
    if request.method == 'POST':
        username = request.POST['User_name']
        password = request.POST['Password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            if user.is_staff:
                auth.login(request,user)
                return HttpResponse("Admin here")
            else:
                auth.login(request,user)
                return redirect('emp_dashboard')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('emp_login')
    
    else:
        return render(request, 'emp/emp_login.html')

def emp_dashboard(request):
    user=request.user
    task = tasks.objects.filter(emp_con=user.id)
    return render(request,'emp/employee-dashboard.html',{'task':task})

def emp_leaves(request):
    user = request.user
    if request.method == "POST":
        leave_type = request.POST["leave_type"]
        leave_from = request.POST["from"]
        leave_to = request.POST["to"]
        leave_reason = request.POST["leave_reason"]

        leve = leaves(emp_con = user,leave_type = leave_type,from_date = leave_from,to_date=leave_to,reson = leave_reason,Status='Pending to Approve')
        leve.save()
        lev = leaves.objects.filter(emp_con = user)
        context = {
            'lev': lev
        }

        messages.info(request,"Leave added successfully")
        return render(request,'emp/leaves.html',context)
    else:
        lev = leaves.objects.filter(emp_con = user)
        context = {
            'lev': lev
        }
        return render(request,'emp/leaves.html',context)

def emp_projects(request):

    pro= project.objects.all()
    return render(request,'emp/projects.html',{'project':pro})

def emp_payslip(request):
    user = request.user
    pe = get_object_or_404(Employee, connection=user)
    
    pay_slip = Pay_slip.objects.filter(emp_id = pe.id).last()
    print("THIS IS PAYSLIP OBJECT : ",pay_slip)
    context = {
        'pay_slip' : pay_slip
    }

    return render(request,'emp/salary-view.html',context)



def emp_profile(request):
    user = request.user
    userr = get_object_or_404(Employee, connection=user)
    context = {
        'userr' : userr
    }
    return render(request,'emp/profile.html',context)
   
def emp_notification(request):
    notice= Notice.objects.all()
    return render(request,'emp/notifications-settings.html',{'notice':notice})












def emp_attend(request):
    user = request.user
    emp_id = user.employee.id
    attend = Attendance.objects.filter(emp_iid = emp_id)[::-1]
    context = {
        'attend' : attend
    }
    return render(request,'emp/emp_attend.html',context)






def payment(request):
    user = request.user
    emp_id = user.employee.id
    pay = Pay_slip.objects.filter(emp_id = emp_id)
    context = {
        'pay' : pay
    }
    return render(request,'emp/payment.html',context)