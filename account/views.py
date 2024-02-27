from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import *
from emailsend import OTGGenerator

# Create your views here.


def RegisterStaff(request):
    try:
        if request.method=='POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]

            if password==confirm_password:                                
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username taken')
                    return redirect("register")  
                
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,  
                        password=password,
                        first_name=first_name,
                        last_name=last_name
                        )
                    user.is_staff=True
                    user.save()

                    OTGGenerator([email], "SUCCESSFUL REGISTRATION!!!", """We are pleased to notify you that your staff account registration on Omotola Cathedral has been successfully completed. Please sign in to continue your browsing experience as a staff on our website and do keep your login details safe. Thank you""")
                    messages.success(request, 'Account created. Please log in')
                    return redirect("login")  

            else:
                messages.error(request, 'Password not the same')
                return redirect("register") 
            
        elif request.method=='GET': 
            return render(request, "register.html") 

    except Exception as ex:
        print(ex)        

       

  
def LoginStaff(request):
    try:
        if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']
            
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)

                request.session["userId"] = user.id
                request.session["username"] = user.username
                request.session["email"] = user.email
                email = request.session["email"]

                OTGGenerator([email], "SUCCESSFUL LOGIN!!!", """We are pleased to notify you that you have successfully logged into your staff account on Omotola Cathedral. Please keep your login details safe. Thank you.""")
                return redirect("home")
            
            else:
                messages.error(request, 'Incorrect username or password')
                return render(request, "login.html") 
            
        elif request.method=='GET':
            return render(request, "login.html") 
        
    except Exception as ex:
        print(ex)




def LogoutStaff(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    auth.logout(request)
    return redirect("home")        
    



def GetAllStaff(request):
    try:
        getallstaffs = User.objects.all()
        return render(request, "", {})                       #check  
    
    except Exception as ex:
        print(ex)




def GetById(request, id):
    try:
        getidstaff = User.objects.get(pk = id)
        return render(request, "", {})                       #check

    except Exception as ex:
        print(ex)




def DeleteStaff(request, id):
    try:
        deletestaff = User.objects.get(pk = id).delete()

        messages.error(request, 'Staff Deleted')
        return redirect("")                                  #check
    
    except Exception as ex:
        print(ex)