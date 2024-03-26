from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from church.models import *
from emailsend import OTGGenerator
from base64converter import CustomInMemoryBase64Converter

# Create your views here.


def adminAnnouncement(request):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            announcement = Announcement.objects.filter(is_removed=False)
            return render(request, "admin/admin_announcement.html", {"announcements": announcement})
        
        except Exception as ex:
            print(ex)

    return redirect("login")



def newAnnouncement(request):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            if request.method == "POST":
                image_path = request.FILES.get('event_image')
                image = CustomInMemoryBase64Converter(image_path)

                user_id = request.session["userId"]
                user = User.objects.get(pk = user_id)

                announcement = Announcement(
                    event_announcement=image,          
                    created_by=user,
                )
                announcement.save()

                messages.success(request, "Announcement saved successfully")
                return redirect("new-announcement")
                
            else:
                return render(request, "admin/admin_new_announcement.html", {})
        
        except Exception as ex:
            print(ex)

    return redirect("login")



def updateAnnouncement(request, id):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            if request.method=='POST':
                image_path = request.FILES.get('event_image')
                image = CustomInMemoryBase64Converter(image_path)

                if len(image) != 0:
                    announcement = Announcement.objects.filter(id = id).first()
                    announcement.event_announcement=image
                    announcement.save()

                    messages.success(request, 'Announcement updated successfully')
                    return redirect("admin-announcement")
                return redirect("admin-announcement")

            elif request.method=='GET':
                announcement = Announcement.objects.get(pk = id)
                return render(request, "admin/admin_edit_announcement.html", {"announcement": announcement})

        except Exception as ex:
            print(ex)

    return redirect("login")



def deleteAnnouncement(request, id):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            announcement = Announcement.objects.get(pk = id)
            announcement.is_removed = True
            announcement.save()

            messages.error(request, 'Announcement Deleted')
            return redirect("admin-announcement")                                                 
        
        except Exception as ex:
            print(ex)

    return redirect("login")






def adminEvent(request):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            event = Event.objects.filter(is_removed=False)
            return render(request, "admin/admin_event.html", {"events": event})
        
        except Exception as ex:
            print(ex)

    return redirect("login")



def newEvent(request):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            if request.method == "POST":
                periodic = request.POST["periodic_display"]
                service = request.POST["service_display"]

                user_id = request.session["userId"]
                user = User.objects.get(pk = user_id)

                event = Event(
                    periodic_display=periodic,
                    service_display=service,
                    created_by=user,
                )
                event.save()

                messages.success(request, "Event saved successfully")
                return redirect("new-event")
                
            else:
                return render(request, "admin/admin_new_event.html", {})
        
        except Exception as ex:
            print(ex)

    return redirect("login")



def updateEvent(request, id):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            if request.method=='POST':
                periodic = request.POST["periodic_display"]
                service = request.POST["service_display"]
                
                if len(periodic) != 0:
                    event = Event.objects.filter(id = id).first()
                    event.periodic_display=periodic
                    event.service_display=service
                    event.save()

                    messages.success(request, 'Event updated successfully')
                    return redirect("admin-event")
                return redirect("admin-event")

            elif request.method=='GET':
                event = Event.objects.get(pk = id)
                return render(request, "admin/admin_edit_event.html", {"event": event})

        except Exception as ex:
            print(ex)

    return redirect("login")



def deleteEvent(request, id):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            event = Event.objects.get(pk = id)
            event.is_removed = True
            event.save()

            messages.error(request, 'Event Deleted')
            return redirect("admin-event")                                                 
        
        except Exception as ex:
            print(ex)

    return redirect("login")






def adminBirthday(request):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            birthday = Birthday.objects.filter(is_removed=False)             
            return render(request, "admin/admin_birthday.html", {"birthdays": birthday})
        
        except Exception as ex:
            print(ex)

    return redirect("login")



def newBirthday(request):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            if request.method == "POST":
                image_path = request.FILES.get('birthday_image')
                image = CustomInMemoryBase64Converter(image_path)

                user_id = request.session["userId"]
                user = User.objects.get(pk = user_id)

                birthday = Birthday(
                    image=image,          
                    created_by=user,
                )
                birthday.save()

                messages.success(request, "Celebrant saved successfully")
                return redirect("new-birthday")
            
            else:
                return render(request, "admin/admin_new_birthday.html", {})
        
        except Exception as ex:
            print(ex)

    return redirect("login")



def updateBirthday(request, id):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            if request.method=='POST':
                image_path = request.FILES.get('birthday_image')
                image = CustomInMemoryBase64Converter(image_path)
                
                if len(image) != 0:
                    birthday = Birthday.objects.filter(id = id).first()
                    birthday.image=image
                    birthday.save()

                    messages.success(request, 'Celebrant updated successfully')
                    return redirect("admin-birthday")
                return redirect("admin-birthday")

            elif request.method=='GET':
                birthday = Birthday.objects.get(pk = id)
                return render(request, "admin/admin_edit_birthday.html", {"birthday": birthday})

        except Exception as ex:
            print(ex)

    return redirect("login")



def deleteBirthday(request, id):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            birthday = Birthday.objects.get(pk = id)
            birthday.is_removed = True
            birthday.save()

            messages.error(request, 'Celebrant Deleted')
            return redirect("admin-birthday")                                                 
        
        except Exception as ex:
            print(ex)

    return redirect("login")






def adminTestimony(request):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            testimony = Testimony.objects.filter(is_removed=False).order_by("-date_created")
            return render(request, "admin/admin_testimonies.html", {"testimonys": testimony})
        
        except Exception as ex:
            print(ex)

    return redirect("login")



def newTestimony(request):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            if request.method == "POST":
                testifier = request.POST["testifier"]
                content = request.POST["content"]

                user_id = request.session["userId"]
                user = User.objects.get(pk = user_id)

                testimony = Testimony(
                    testifier_name=testifier,
                    testimony_content=content,
                    created_by=user,
                )
                testimony.save()

                messages.success(request, "Testimony saved successfully")
                return redirect("new-testimony")
                
            else:
                return render(request, "admin/admin_new_testimony.html", {})
        
        except Exception as ex:
            print(ex)

    return redirect("login")



def updateTestimony(request, id):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            if request.method=='POST':
                testifier = request.POST["testifier"]
                content = request.POST["content"]
                
                if len(testifier) and len(content) != 0:
                    testimony = Testimony.objects.filter(id = id).first()
                    testimony.testifier_name=testifier
                    testimony.testimony_content=content
                    testimony.save()

                    messages.success(request, 'Testimony updated successfully')
                    return redirect("admin-testimony")
                return redirect("admin-testimony")

            elif request.method=='GET':
                testimony = Testimony.objects.get(pk = id)
                return render(request, "admin/admin_edit_testimonies.html", {"testimony": testimony})

        except Exception as ex:
            print(ex)

    return redirect("login")



def deleteTestimony(request, id):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            testimony = Testimony.objects.get(pk = id)
            testimony.is_removed = True
            testimony.save()

            messages.error(request, 'Testimony Deleted')
            return redirect("admin-testimony")                                                 
        
        except Exception as ex:
            print(ex)

    return redirect("login")






def adminOffice(request):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            office = Office.objects.filter(is_removed=False).order_by("date_created")
            return render(request, "admin/admin_office.html", {"offices": office})
        
        except Exception as ex:
            print(ex)

    return redirect("login")



def newOffice(request):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            if request.method == "POST":
                office_title = request.POST["office"]

                user_id = request.session["userId"]
                user = User.objects.get(pk = user_id)

                office = Office(
                    title=office_title,          
                    created_by=user,
                )
                office.save()

                messages.success(request, "Office saved successfully")
                return redirect("new-office")
                
            else:
                return render(request, "admin/admin_new_office.html")
        
        except Exception as ex:
            print(ex)

    return redirect("login")



def updateOffice(request, id):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            if request.method=='POST':
                office_title = request.POST["office"]
                
                if len(office_title) != 0:
                    office = Office.objects.filter(id = id).first()
                    office.title=office_title
                    office.save()

                    messages.success(request, 'Office updated successfully')
                    return redirect("admin-office")
                return redirect("admin-office")

            elif request.method=='GET':
                office = Office.objects.get(pk = id)
                return render(request, "admin/admin_edit_office.html", {"office": office})

        except Exception as ex:
            print(ex)

    return redirect("login")



def deleteOffice(request, id):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            office = Office.objects.get(pk = id)
            office.is_removed = True
            office.save()

            messages.error(request, 'office Deleted')
            return redirect("admin-office")                                                 
        
        except Exception as ex:
            print(ex)

    return redirect("login")






def adminTwelvePillar(request):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            twelvePillar = Team.objects.filter(is_removed=False).order_by("date_created")
            return render(request, "admin/admin_twelve_pillars.html", {"twelvePillars": twelvePillar})
        
        except Exception as ex:
            print(ex)

    return redirect("login")



def newTwelvePillar(request):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            if request.method == "POST":
                office = request.POST["office"]
                splitted_office = office.split("-")
                office_id = splitted_office[0]
                office_title = splitted_office[1]

                name = request.POST["name"]

                image_path = request.FILES.get('office_image')
                image = CustomInMemoryBase64Converter(image_path)

                user_id = request.session["userId"]
                user = User.objects.get(pk = user_id)

                if Team.objects.filter(office_id=office_id).exists():
                    messages.error(request, 'Selected office already exist')
                    return redirect("new-twelve-pillar")

                else:
                    twelvePillar = Team(
                        office_id=int(office_id),          
                        name=name,
                        image=image,
                        created_by=user,
                    )
                    twelvePillar.save()

                    messages.success(request, "Member saved successfully")
                    return redirect("new-twelve-pillar")
                
            else:
                office = Office.objects.filter(is_removed=False)
                return render(request, "admin/admin_new_twelve_pillars.html", {"offices": office})
        
        except Exception as ex:
            print(ex)

    return redirect("login")



def updateTwelvePillar(request, id):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            if request.method=='POST':
                name = request.POST["name"]
                office = request.POST["office"]
                splitted_office = office.split("-")
                office_id = splitted_office[0]
                office_title = splitted_office[1]

                image_path = request.FILES.get('office_image')
                image = CustomInMemoryBase64Converter(image_path)
                
                if len(name) and len(office) != 0:
                    twelvePillar = Team.objects.filter(id = id).first()
                    twelvePillar.office.title=office_title
                    twelvePillar.name=name
                    twelvePillar.image=image
                    twelvePillar.save()

                    messages.success(request, 'Member updated successfully')
                    return redirect("admin-twelve-pillar")
                return redirect("admin-twelve-pillar")

            elif request.method=='GET':
                twelvePillar = Team.objects.get(pk = id)
                office = Office.objects.filter(is_removed=False)
                return render(request, "admin/admin_edit_twelve_pillars.html", {"twelvePillar": twelvePillar, "offices": office})

        except Exception as ex:
            print(ex)

    return redirect("login")



def deleteTwelvePillar(request, id):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            twelvePillar = Team.objects.get(pk = id).delete()
            # twelvePillar.is_removed = True
            # twelvePillar.save()

            messages.error(request, 'Member Deleted')
            return redirect("admin-twelve-pillar")                                                 
        
        except Exception as ex:
            print(ex)

    return redirect("login")






def adminSermonExcerpt(request):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            sermonExcerpt = Sermon.objects.filter(is_removed=False).order_by("-date_created")
            return render(request, "admin/admin_sermon_excerpt.html", {"sermonExcerpts": sermonExcerpt})
    
        except Exception as ex:
            print(ex)

    return redirect("login")



def newSermonExcerpt(request):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            if request.method == "POST":
                service_type = request.POST["service_type"]
                image_path = request.FILES.get('sermoner_picture')
                image = CustomInMemoryBase64Converter(image_path)

                sermoner = request.POST["sermoner"]
                topic = request.POST["topic"]
                content = request.POST["content"]

                user_id = request.session["userId"]
                user = User.objects.get(pk = user_id)

                sermonExcerpt = Sermon(
                    service_type=service_type,
                    sermoner_picture=image,
                    sermoner=sermoner,
                    topic=topic,
                    content=content,
                    created_by=user,
                )
                sermonExcerpt.save()

                messages.success(request, "Sermon excerpt saved successfully")
                return redirect("new-sermon-excerpt")
                
            else:
                return render(request, "admin/admin_new_sermon_excerpt.html", {})
        
        except Exception as ex:
            print(ex)

    return redirect("login")



def updateSermonExcerpt(request, id):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            if request.method=='POST':
                service_type = request.POST["service_type"]
                image_path = request.FILES.get('sermoner_picture')
                image = CustomInMemoryBase64Converter(image_path)

                sermoner = request.POST["sermoner"]
                topic = request.POST["topic"]
                content = request.POST["content"]
                
                if len(sermoner) and len(content) != 0:
                    sermonExcerpt = Sermon.objects.filter(id = id).first()
                    sermonExcerpt.service_type=service_type
                    sermonExcerpt.sermoner_picture=image
                    sermonExcerpt.sermoner=sermoner
                    sermonExcerpt.topic=topic
                    sermonExcerpt.content=content
                    sermonExcerpt.save()

                    messages.success(request, 'Sermon excerpt updated successfully')
                    return redirect("admin-sermon-excerpt")
                return redirect("admin-sermon-excerpt")

            elif request.method=='GET':
                sermonExcerpt = Sermon.objects.get(pk = id)
                return render(request, "admin/admin_edit_sermon_excerpt.html", {"sermonExcerpt": sermonExcerpt})

        except Exception as ex:
            print(ex)

    return redirect("login")



def deleteSermonExcerpt(request, id):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            sermonExcerpt = Sermon.objects.get(pk = id)
            sermonExcerpt.is_removed = True
            sermonExcerpt.save()

            messages.error(request, 'Sermon Excerpt Deleted')
            return redirect("admin-sermon-excerpt")                                                 
        
        except Exception as ex:
            print(ex)

    return redirect("login")






def registerStaff(request):
    try:
        if request.method=='POST':
            # first_name = request.POST["first_name"]
            # last_name = request.POST["last_name"]
            email = request.POST['email']
            
            # splitted_email = email.split("@")
            # uname = splitted_email[0]

            username = request.POST['username']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

            if password==confirm_password:                                
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email taken')
                    return redirect("register")  
                
                else:
                    user = User.objects.create_user(
                        # first_name=first_name,
                        # last_name=last_name,
                        email=email,
                        username=username,  
                        password=password,
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
            return render(request, "admin/register.html") 

    except Exception as ex:
        print(ex)        

       

  
def loginStaff(request):
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
                return redirect("admin-testimony")
            
            else:
                messages.error(request, 'Incorrect username or password')
                return render(request, "admin/login.html") 
            
        elif request.method=='GET':
            return render(request, "admin/login.html") 
        
    except Exception as ex:
        print(ex)




def logoutStaff(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    auth.logout(request)
    return redirect("login")    




def getAllStaffs(request):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            staff = User.objects.filter(is_active=True)
            return render(request, "admin/admin_profiles.html", {"staffs": staff})
        
        except Exception as ex:
            print(ex)

    return redirect("login")




def deleteStaff(request, id):
    session_keys = list(request.session.keys())
    if len(session_keys) != 0:
        try:
            user = User.objects.get(pk = id)
            user.is_active = False
            user.save()

            messages.error(request, 'Staff Deleted')
            return redirect("get-all-staffs")               
        
        except Exception as ex:
            print(ex)

    return redirect("login")