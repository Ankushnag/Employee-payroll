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



def Base(request):
    return render(request, 'payroll/base.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            if user.is_staff:
                return redirect("dashboard")
            else:
                messages.info(request,"Invalid credentials")
                return redirect('login')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    
    else:
        return render(request, 'payroll/login.html')


def logout(request):
    auth.logout(request)
    return redirect('emp_login')


def Register(request):
    return render(request, 'payroll/register.html')


@login_required(login_url='login')
def Dashboard(request):
    cnt = Employee.objects.all().count()
    print("COUNT  ", cnt)

    now = datetime.datetime.now()
    today_date = (now.strftime("%Y-%m-%d"))
    print(today_date)

    
    today_present = Attendance.objects.filter(date = today_date,presenty='Present').count()
    print("Today present :",today_present)

    today_absent = Attendance.objects.filter(date = today_date,presenty='Absent').count()
    
    today_absent = cnt - today_present


    attendance = Attendance.objects.filter(date=today_date)


    context = {
        'cnt' :cnt,
        'today_present' : today_present,
        'today_absent' : today_absent,
        'attendance' : attendance,


    }
    return render(request, 'payroll/dashboard.html',context)


@login_required(login_url='login')
def Add_employee(request):
    field = Fields.objects.all()
    context = {
        'field' : field
    }
    return render(request, 'payroll/add_employee.html',context)


@login_required(login_url='login')
def Emp_add(request):
    try:
        if request.method == 'POST':
            fname = request.POST['fname']
            lname = request.POST['lname']
            gender = request.POST['gender']
            date = request.POST['date']
            education = request.POST['education']
            email = request.POST['email']
            field = request.POST['field']
            payment = request.POST['payment']
            phone = request.POST['phone']
            address = request.POST['address']
            username = request.POST['username']
            password = request.POST['password']

            emp_user = User.objects.create_user(username=username, password=password,first_name=fname,last_name=lname)
            emp_user.save()
            emp = Employee(connection=emp_user,emp_name=fname,
            emp_last_name=lname,
            emp_gender = gender,
            emp_dob=date,
            emp_education=education,
            emp_email = email,
            emp_field= field,
            emp_payment=payment,
            emp_phone = phone,
            emp_address= address
            )
            emp.save()
            messages.info(request,"Employee added successfully")
            return redirect('add_employee')
    except:
        messages.info(request,"Something wrong")
        return redirect('add_employee')


@login_required(login_url='login')
def Employee_detail(request,myid):
    emp = Employee.objects.get(id = myid)

    context = {
        'emp' : emp
    }
    return render(request, 'payroll/employee_detail.html',context)


@login_required(login_url='login')
def Employee_list(request):
    emp = Employee.objects.all()

    context = {
        'emp' : emp
    }
    return render(request, 'payroll/employee_list.html',context)


@login_required(login_url='login')
def Emp_search(request):
    try:
        #allPosts = courseApp.objects.all()
        query = request.GET['query']
        print("-------------------------",query)
        employee = Employee.objects.filter(emp_name__icontains=query)
        params = {'emp': employee}
        return render(request, 'payroll/employee_list.html', params)
    except:
        return redirect('employee_list')


@login_required(login_url='login')
def Delet_emp(request,myid):
    emp = Employee.objects.get(id = myid)
    emp.delete()

    return redirect('employee_list')


@login_required(login_url='login')
def Add_new_field(request):
    return render(request, 'payroll/add_new_field.html')


@login_required(login_url='login')
def Field_save(request):
    try:
        if request.method == 'POST':
            name = request.POST['field_name']
            explain = request.POST['field_explain']
            
            fields = Fields(field_name = name,explain_field= explain)
            fields.save()

            messages.info(request,"Field added successfully")
            return redirect('add_new_field')
    except:
        messages.info(request,"Something wrong")
        return redirect('add_new_field')


@login_required(login_url='login')
def All_field(request):
    field = Fields.objects.all()

    context = {
        'field' : field
    }
    return render(request, 'payroll/all_field.html',context)


@login_required(login_url='login')
def Delet_field(request,myid):
    field = Fields.objects.get(id = myid)
    field.delete()
    return redirect('all_field')


@login_required(login_url='login')
def Search_field(request):
    try:
        #allPosts = courseApp.objects.all()
        query = request.GET['query']
        print("-------------------------",query)
        field = Fields.objects.filter(field_name__icontains=query)
        params = {'field': field}
        return render(request, 'payroll/all_field.html', params)
    except:
        return redirect('all_field')

    
@login_required(login_url='login')
def Daily_attendance(request):
    return render(request, 'payroll/daily_attendance.html')


@login_required(login_url='login')
def Attendance_save(request):
    try:
        if request.method == 'POST':
            emp_id = request.POST['emp_id']
            datee = request.POST['date']
            attend = request.POST['attend']
            
            attendance = Attendance(emp_iid=emp_id,date=datee, presenty = attend)
            attendance.save()
            messages.info(request,"Attendance added successfully")
            return redirect('daily_attendance')
    except:
        messages.info(request,"Something wrong")
        return redirect('daily_attendance')


@login_required(login_url='login')
def Attendance_report(request):
    attendance = Attendance.objects.all()

    context = {
        'attendance' : attendance
    }
    return render(request, 'payroll/attendance_report.html',context)


@login_required(login_url='login')
def Search_attendance(request):
    try:
        #allPosts = courseApp.objects.all()
        query = request.GET['query']
        print("-------------------------",query)
        attendance = Attendance.objects.filter(emp_iid__icontains=query)
        params = {'attendance': attendance}
        return render(request, 'payroll/attendance_report.html',params)
    except:
        return redirect('attendance_report')
    

@login_required(login_url='login')
def Create_payslip(request):
    return render(request, 'payroll/create_payslip.html')



@login_required(login_url='login')
def Payslip_save(request):
    
    if request.method == 'POST':
        emp_id = request.POST["empid"]
        emp_name = request.POST["name"]
        basic_salary = request.POST["basic_salary"]
        HRA = request.POST["HRA"]
        other_allow = request.POST["other"]
        total_earning = request.POST["amount"]
        phone = request.POST["phone"]
        amount = request.POST["amount"]
        email = request.POST["email"]
        
        pay_slip =Pay_slip(emp_id = emp_id,emp_name =emp_name,basic_salary = basic_salary,HRA=HRA,other_allow=other_allow,total_earninig=total_earning,phone=phone,amount=amount,email = email)
        pay_slip.save()
      
        messages.info(request,"Payment added successfully")
        return redirect('create_payslip')
   

@login_required(login_url='login')
def Payslip_delet(request,myid):
    pay_slip = Pay_slip.objects.get(id = myid)
    pay_slip.delete()

    return redirect('payslip_list')


@login_required(login_url='login')
def Payslip_list(request):
    payslip = Pay_slip.objects.all()

    context = {
        'payslip' : payslip
    }

    return render(request, 'payroll/payslip_list.html',context)


@login_required(login_url='login')
def Add_new_expenses(request):
    return render(request, 'payroll/add_new_expenses.html')


@login_required(login_url='login')
def Expense_added(request):
  
    if request.method == 'POST':
        a_payto = request.POST['payto']
        a_reason = request.POST['reason']
        a_amount = request.POST['amount']
        a_phone = request.POST['phone']
        a_email = request.POST['email']
        # a_date = request.POST['date']

        expenses = Expenses(amount = a_amount,pay_to = a_payto,Phone = a_phone,email = a_email,describe_payment = a_reason)
        expenses.save()
        
        messages.info(request,"Expense added successfully")
        return redirect('add_new_expenses')
   

@login_required(login_url='login')
def All_expenses(request):
    expenses = Expenses.objects.all()
    context = {
        'expense' : expenses
    }
    return render(request, 'payroll/all_expenses.html',context)


@login_required(login_url='login')
def Delet_exp(request,myid):
    expenses = Expenses.objects.get(id = myid)
    expenses.delete()
    return redirect('all_expenses')


@login_required(login_url='login')
def Message(request):
    if request.method == "POST":
        title = request.POST["title"]
        detail =  request.POST["detail"]
        posted_by =  request.POST["posted_by"]
        date = request.POST["date"]
        msg = Notice(title = title,detail = detail,posted_by = posted_by,date = date)
        msg.save()
        messages.info(request,"Notice addedd successfuly")
        return render(request, 'payroll/message.html')
    else:

        return render(request, 'payroll/message.html')


@login_required(login_url='login')
def Noticeboard(request):
    notice= Notice.objects.all()
    return render(request, 'payroll/noticeboard.html',{'notice':notice})






def personal_detail_add(request):
    if request.method == "POST":
        try:
            empid = request.POST["empid"]
            tel = request.POST["tel"]
            nationality = request.POST["nationality"]
            religion = request.POST["religion"]
            marital_status = request.POST["marital_status"]
            photo = request.FILES['photo']
            emp = Employee.objects.get(id = empid)
            per = Employee_personal_info(emp =emp,tel =tel,nationality = nationality,religion = religion,marital_status=marital_status,photo=photo)
            per.save()
            messages.info(request,"Personal Detail Addedd successfully")
        except:
            messages.info(request,"Personal Detail already for this employee please Update from employee list")
    else:
        pass

    return render(request,'payroll/personal_detail_add.html')





def bank_detail_add(request):
    if request.method == "POST":
        try:
            empid = request.POST['empid']
            bank_name = request.POST["bank_name"]
            bank_ac_no = request.POST["bank_ac_no"]
            ifsc = request.POST["ifsc"]
            pan = request.POST["pan"]
            emp = Employee.objects.get(id = empid)

            bank = Employee_bank_info(emp =emp,bank_name = bank_name,bank_ac_no=bank_ac_no,ifsc = ifsc,pan = pan)
            bank.save()
            messages.info(request,"Bank Detail Addedd successfully")
        except:
            messages.info(request,"Bank detail already added to this employee please edit from employee list")
    
    else:
        pass
    return render(request,'payroll/bank_detail_add.html')