from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from .models import Contact,services

# Create your views here.


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,"about.html")

def reg(request):
    if request.method=='POST':
        Username=request.POST['Username']
        Age=request.POST['Age']
        Email=request.POST['Email']
        Password=request.POST['Password']
       
        myuser=User.objects.create_user(Username,Email)
        myuser.username=Username
        myuser.save()
        messages.success(request,"Your account has been successfully created.")
        return render(request,'registration.html')
    else:
        return render(request,'registration.html')

def login(request):
    if request.method=="POST":
       Email=request.POST['Email']
       Password=request.POST['Password']
       user=auth.authenticate(email=Email,password=Password)
       
       if user is not None:
         auth.login(request,user)
         Email=user.email
        
       else:
         messages.success(request,"Logged in Successfully!")
         return render(request,'home.html')
    
    return render (request,'login.html')  

def con(request):
    if request.method=='POST':
       models=Contact(request.POST)
       name=request.POST['name']
       email=request.POST['email']
       subject=request.POST['subject']
       message=request.POST['message']
       Contact(name=name,email=email,subject=subject,message=message).save()
       messages.success(request,"Thanks for contact with us!")
       return render(request,'contact.html')
    else:
        return render(request,'contact.html')


def home(request):
    return render(request,"home.html")

def booking(request):
    return render(request,"booking.html") 

def servicepage(request):
   
    context = {
        'service': services.objects.all()
    }
    return render(request, 'services.html', context)   





