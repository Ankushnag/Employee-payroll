from django.contrib import admin

# Register your models here.
from .models import Employee, Employee_bank_info, Employee_personal_info, Fields,Pay_slip, Expenses,Notice, Attendance


class EmployeeAdmin(admin.ModelAdmin):
        list_per_page = 10
        #list_display = []
        list_filter = ['emp_education']
        search_fields = ['emp_name']
admin.site.register(Employee,EmployeeAdmin) 


class FieldsAdmin(admin.ModelAdmin):
        list_per_page = 10
        #list_display = []
        list_filter = []
        search_fields = []
admin.site.register(Fields,FieldsAdmin) 


class Pay_slipAdmin(admin.ModelAdmin):
        list_per_page = 10
        #list_display = []
        list_filter = []
        search_fields = []
admin.site.register(Pay_slip,Pay_slipAdmin) 


class ExpensesAdmin(admin.ModelAdmin):
        list_per_page = 10
        #list_display = []
        list_filter = []
        search_fields = []
admin.site.register(Expenses,ExpensesAdmin) 


class NoticeAdmin(admin.ModelAdmin):
        list_per_page = 10
        #list_display = []
        list_filter = []
        search_fields = []
admin.site.register(Notice,NoticeAdmin) 


class AttendanceAdmin(admin.ModelAdmin):
        list_per_page = 10
        #list_display = []
        list_filter = ['emp_iid','date']
        search_fields = ['emp_iid']
admin.site.register(Attendance,AttendanceAdmin) 







admin.site.register(Employee_personal_info)

admin.site.register(Employee_bank_info)