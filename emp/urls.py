from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth import urls
from . import views





urlpatterns = [
    path('',views.emp_login,name='emp_login'),
    path('dashboard',views.emp_dashboard,name='emp_dashboard'),
    path('leaves',views.emp_leaves,name='leaves'),
    path('projects',views.emp_projects,name='emp_projects'),
    path('payslip',views.emp_payslip,name='emp_payslip'),
    
    path('notification',views.emp_notification,name='notification'),

    path('emp_attend',views.emp_attend,name='emp_attend'),

    path('payment',views.payment,name='payment'),


   


]
