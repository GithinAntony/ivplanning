from django.urls import path
from . import views

app_name='index'
urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('find-industry',views.find_industry,name='find_industry'),
    path('find-industry-view/<int:id>',views.find_industry_view,name='find_industry_view'),
    path('find-hotels',views.find_hotel,name='find_hotel'),
    path('find-hotels-view/<int:id>',views.find_hotel_view,name='find_hotel_view'),
]
