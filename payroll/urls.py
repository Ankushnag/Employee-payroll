from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    #################BASE FILE
    path('base',views.Base, name='base'),
    path('',views.Login, name='login'),


    ################LOGIN REGISTER
    path('login',views.Login, name='login'),
    path('logout',views.logout, name='logout'),
    path('register',views.Register, name='register'),


    #####################DASHBOARD
    path('dashboard',views.Dashboard, name='dashboard'),


    ####################employee
    path('add_employee',views.Add_employee, name='add_employee'),
    path('emp_add',views.Emp_add, name='emp_add'),
    path('employee_detail/<int:myid>/',views.Employee_detail, name='employee_detail'),
    path('delet_emp/<int:myid>/',views.Delet_emp, name='delet_emp'),
    path('employee_list',views.Employee_list, name='employee_list'),
    path('emp_search',views.Emp_search, name='emp_search'),


    #############################field
    path('add_new_field',views.Add_new_field, name='add_new_field'),
    path('field_save',views.Field_save, name='field_save'),
    path('all_field',views.All_field, name='all_field'),
    path('delet_field/<int:myid>/',views.Delet_field, name='delet_field'),
    path('search_field',views.Search_field, name='search_field'),



    ###########################Attendance
    path('daily_attendance',views.Daily_attendance, name='daily_attendance'),
    path('attendance_report',views.Attendance_report, name='attendance_report'),
    path('attendance_save',views.Attendance_save, name='attendance_save'),
    path('search_attendance',views.Search_attendance, name='search_attendance'),



    ############################PAYSLIP
    path('create_payslip',views.Create_payslip, name='create_payslip'),
    path('payslip_list',views.Payslip_list, name='payslip_list'),
    path('payslip_save',views.Payslip_save, name='payslip_save'),
    path('payslip_delet/<int:myid>/',views.Payslip_delet, name='payslip_delete'),



    ##########################EXPENSES
    path('add_new_expenses',views.Add_new_expenses, name='add_new_expenses'),
    path('expense_added',views.Expense_added, name="expense_added"),
    path('all_expenses',views.All_expenses, name='all_expenses'),
    path('delet_exp/<int:myid>/',views.Delet_exp, name='delet_exp'),



    ###################MESSAGE NOTIFICATIONS EXTRA
    path('message',views.Message, name='message'),
    path('noticeboard',views.Noticeboard, name='noticeboard'),

    path('personal_detail_add',views.personal_detail_add, name='personal_detail_add'),

    path('bank_detail_add',views.bank_detail_add, name='bank_detail_add'),





]
