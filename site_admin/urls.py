from django.urls import path
from . import views

app_name='site_admin'
urlpatterns = [
    path('',views.login,name='login'),
    path('login',views.login,name='login'),    
]
