from django.contrib import admin
from .models import tasks,leaves,project

# Register your models here.
admin.site.register(tasks) 
admin.site.register(leaves) 
admin.site.register(project) 
