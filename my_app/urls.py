from . import views
from django.urls import path


urlpatterns=[
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('home',views.home,name="home"),
    path('booking',views.booking,name="booking"),
    path('registration',views.reg,name="registration"),
    path('login',views.login,name="login"),
    path('contact',views.con,name="contact"),
    path('services/',views.servicepage,name='servicepage'),

    
  
]