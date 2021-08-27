from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth import urls


from emp .views import emp_profile




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('payroll.urls')),
    path('emp',include('emp.urls')),

    path('profile',emp_profile,name='profile'),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

