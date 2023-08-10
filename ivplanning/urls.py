from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin2022/', admin.site.urls),
    path('',include('index.urls'),),
    path('industry/',include('industry.urls'),),
    path('colleges/',include('colleges.urls'),),    
#    path('admin2022/',include('site_admin.urls',namespace='site_admin'),)
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
