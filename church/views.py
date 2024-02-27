from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import *
from emailsend import OTGGenerator
from base64converter import CustomInMemoryBase64Converter
from datetime import datetime, timezone

# Create your views here.


def home(request):
    try:
        event = Event.objects.first()

        # valid = event.date_created.strftime('%A') < datetime.now(timezone.utc).strftime('%A')
        # print(type(datetime.now(timezone.utc).strftime('%A')))
        # print(type(event.date_created.strftime('%A')))
        # print(event.date_created.strftime('%A'))
        # print(datetime.now(timezone.utc).strftime('%A'))
        # if valid:
        #     event.service_display = None
        #     event.save()
        return render(request, "index.html", {"event": event})
    
    except Exception as ex:
        print(ex)



def about(request):
    try:
        return render(request, "about.html")
    
    except Exception as ex:
        print(ex)



def contact(request):
    try:
        return render(request, "contact.html")
    
    except Exception as ex:
        print(ex)



def testimonies(request):
    try:
        return render(request, "testimonies.html")

    except Exception as ex:
        print(ex)



def services(request):
    try:
        return render(request, "services.html")
    
    except Exception as ex:
        print(ex)



def twelvePillars(request):
    try:
        pillar = Team.objects.all().order_by('date_created')
        return render(request, "twelve-pillars.html", {"pillars": pillar})
    
    except Exception as ex:
        print(ex)



def fourCorners(request):
    try:
        return render(request, "four-corners.html")
    
    except Exception as ex:
        print(ex)



def adminHome(request):
    try:
        return render(request, "admin.html", {})
    
    except Exception as ex:
        print(ex)   



def prayerRequest(request):
    try:
        if request.method=="POST":
            name = request.POST['name']
            country = request.POST['country']
            email = request.POST['email']
            phone_number = request.POST['phone_no']
            message = request.POST['message']

            prayer_request = PrayerRequest(
                name=name,
                country=country,
                email=email,
                phone_number=phone_number,
                message=message
                )
            prayer_request.save()

            OTGGenerator([email], "SUCCESSFUL SUBMISSION OF PRAYER REQUEST!!!", """We kindly inform you that your prayer request has been sent to the church for prior attention. Keep your faith steadfast in the Lord Jesus. God bless you.""")
            return render(request, "index.html")

    except Exception as ex:
        print(ex)



def devotionalLetter(request):
    try:
        if request.method=="POST":
            email = request.POST['newsletter_email']

            devotional_letter = DevotionalLetter(
                email=email
                )
            devotional_letter.save()

            OTGGenerator([email], "SUBSCRIBTION TO DEVOTIONAL LETTER!!!", """We kindly inform you that you have subscribe to our devotional letter for frequent biblical and spiritual devotions.""")
            return render(request, "index.html")

    except Exception as ex:
        print(ex)


    






# #general views

# def CreateGeneral(request):
#     try:
#         if request.method=='POST':
#             myFaviconPath = request.POST['favicon']
#             favicon = CustomInMemoryBase64Converter(myFaviconPath)

#             myLogoPath = request.POST['church_logo']
#             church_logo = CustomInMemoryBase64Converter(myLogoPath)

#             general = GeneralView(
#                 favicon=favicon, 
#                 church_logo=church_logo, 
#                 )
#             general.save()
        
#             messages.success(request, 'Information added successfully')
#             return redirect("admin-home")
            
#         elif request.method=='GET': 
#             return render(request, "")                                        #check (html)

#     except Exception as ex:
#         print(ex)



# def GetAllGeneral(request):
#     try:
#         general = GeneralView.objects.all()
#         return render(request, "", {})                                        #check (html)
    
#     except Exception as ex:
#         print(ex)   



# def GetGeneralById(request, id):
#     try:
#         general = GeneralView.objects.get(pk = id)
#         return render(request, "", {})                                        #check (html)

#     except Exception as ex:
#         print(ex)  



# def UpdateGeneral(request, id):
#     try:
#         if request.method=='POST':
#             myFaviconPath = request.POST['favicon']
#             favicon = CustomInMemoryBase64Converter(myFaviconPath)

#             myLogoPath = request.POST['church_logo']
#             church_logo = CustomInMemoryBase64Converter(myLogoPath)

#             updategeneral = GeneralView.objects.filter(id = id).first()
#             updategeneral.favicon=favicon
#             updategeneral.church_logo=church_logo

#             updategeneral.save
#             messages.success(request, 'Information updated successfully')
#             return redirect("admin-home")
        
#         elif request.method=='GET':
#             return render(request, "")                                         #check (html)

#     except Exception as ex:
#         print(ex)



# def DeleteGeneral(request, id):
#     try:
#         deletegeneral = GeneralView.objects.get(pk = id).delete()

#         messages.error(request, 'Information Deleted')
#         return redirect("")                                                 #check (url name)
    
#     except Exception as ex:
#         print(ex)        






# #home views

# def CreateHome(request):
#     try:
#         if request.method=='POST':
#             front_video = request.POST["front_video"]
#             myFront_imagePath = request.POST['front_image']
#             front_image = CustomInMemoryBase64Converter(myFront_imagePath)

#             evangelism_topic = request.POST["evangelism_topic"]
#             evangelism_content = request.POST["evangelism_content"]
#             myEvangelism_imagePath = request.POST["evangelism_image"]
#             evangelism_image = CustomInMemoryBase64Converter(myEvangelism_imagePath)


#             if HomeView.objects.filter(evangelism_topic=evangelism_topic).exists():
#                 messages.error(request, "Topic already exist")
#                 return redirect("")                                           #check (url name)
            
#             else:
#                 home = HomeView(
#                     front_video=front_video, 
#                     front_image=front_image, 
#                     evangelism_topic=evangelism_topic,
#                     evangelism_content=evangelism_content,
#                     evangelism_image=evangelism_image
#                     )
#                 home.save()
            
#                 messages.success(request, 'Information added successfully')
#                 return redirect("admin-home")
            
#         elif request.method=='GET': 
#             return render(request, "")                                        #check (html)

#     except Exception as ex:
#         print(ex)



# def GetAllHome(request):
#     try:
#         getallhome = HomeView.objects.all()
#         return render(request, "", {})                                        #check (html)
    
#     except Exception as ex:
#         print(ex)
    


# def GetHomeById(request, id):
#     try:
#         getidhome = HomeView.objects.get(pk = id)
#         return render(request, "", {})                                        #check (html)

#     except Exception as ex:
#         print(ex)
    


# def UpdateHome(request, id):
#     try:
#         if request.method=='POST':
#             front_video = request.POST["front_video"]
#             myFront_imagePath = request.POST['front_image']
#             front_image = CustomInMemoryBase64Converter(myFront_imagePath)

#             evangelism_topic = request.POST["evangelism_topic"]
#             evangelism_content = request.POST["evangelism_content"]
#             myEvangelism_imagePath = request.POST["evangelism_image"]
#             evangelism_image = CustomInMemoryBase64Converter(myEvangelism_imagePath)

#             updatehome = HomeView.objects.filter(id = id).first()
#             updatehome.front_video=front_video
#             updatehome.front_image=front_image
#             updatehome.evangelism_topic=evangelism_topic
#             updatehome.evangelism_content=evangelism_content
#             updatehome.evangelism_image=evangelism_image

#             updatehome.save
#             messages.success(request, 'Information updated successfully')
#             return redirect("admin-home")
        
#         elif request.method=='GET':
#             return render(request, "")                                         #check (html)

#     except Exception as ex:
#         print(ex)
    


# def DeleteHome(request, id):
#     try:
#         deletehome = HomeView.objects.get(pk = id).delete()

#         messages.error(request, 'Information Deleted')
#         return redirect("")                                                 #check (url name)
    
#     except Exception as ex:
#         print(ex)
    





# # blog views

# def CreateBlog(request):
#     try:        
#         if request.method=='POST':
#             topic = request.POST["topic"]
#             content = request.POST["content"]
#             myImagePath = request.POST['image']
#             image = CustomInMemoryBase64Converter(myImagePath)

#             if BlogView.objects.filter(topic=topic).exists():
#                 messages.error(request, "Topic already exist")
#                 return redirect("")                                           #check (url name)
            
#             else:
#                 blog = BlogView(
#                     topic=topic, 
#                     content=content, 
#                     image=image, 
#                     )
#                 blog.save()
            
#                 messages.success(request, 'Information added successfully')
#                 return redirect("admin-home")
            
#         elif request.method=='GET': 
#             return render(request, "")                                          #check (html)

#     except Exception as ex:
#         print(ex)
    


# def GetAllBlog(request):
#     try:
#         getallblog = BlogView.objects.all()
#         return render(request, "", {})                                        #check (html)
    
#     except Exception as ex:
#         print(ex)
    


# def GetBlogById(request, id):
#     try:
#         getidblog = BlogView.objects.get(pk = id)
#         return render(request, "", {})                                        #check (html)

#     except Exception as ex:
#         print(ex)
    


# def UpdateBlog(request, id):
#     try:
#         if request.method=='POST':
#             topic = request.POST["topic"]
#             content = request.POST["content"]
#             myImagePath = request.POST['image']
#             image = CustomInMemoryBase64Converter(myImagePath)

#             updateblog = BlogView.objects.filter(id = id).first()
#             updateblog.topic=topic
#             updateblog.content=content
#             updateblog.image=image

#             updateblog.save
#             messages.success(request, 'Information updated successfully')
#             return redirect("admin-home")
        
#         elif request.method=='GET':
#             return render(request, "")                                         #check (html)


#     except Exception as ex:
#         print(ex)
    


# def DeleteBlog(request, id):
#     try:
#         deleteblog = BlogView.objects.get(pk = id).delete()

#         messages.error(request, 'Information Deleted')
#         return redirect("")                                                 #check (url name)

#     except Exception as ex:
#         print(ex)
    





# # media views

# def CreateMedia(request):
#     try:
#         if request.method=='POST':
#             myImagePath = request.POST['image']
#             image = CustomInMemoryBase64Converter(myImagePath)

#             image_description = request.POST["image_description"]
#             video = request.POST["video"]
#             video_description = request.POST["video_description"]

#             media = MediaView(
#                 image=image, 
#                 image_description=image_description, 
#                 video=video, 
#                 video_description=video_description
#                 )
#             media.save()

#             messages.success(request, 'Information added successfully')
#             return redirect("admin-home")
            
#         elif request.method=='GET': 
#             return render(request, "")                                          #check (html)

#     except Exception as ex:
#         print(ex)
    


# def GetAllMedia(request):
#     try:
#         getallmedia = MediaView.objects.all()
#         return render(request, "", {})                                        #check (html)

#     except Exception as ex:
#         print(ex)
    


# def GetMediaById(request, id):
#     try:
#         getidmedia = MediaView.objects.get(pk = id)
#         return render(request, "", {})                                        #check (html)

#     except Exception as ex:
#         print(ex)
    


# def UpdateMedia(request, id):
#     try:
#         if request.method=='POST':
#             myImagePath = request.POST['image']
#             image = CustomInMemoryBase64Converter(myImagePath)

#             image_description = request.POST["image_description"]
#             video = request.POST["video"]
#             video_description = request.POST["video_description"]

#             updatemedia = MediaView.objects.filter(id = id).first()
#             updatemedia.image=image
#             updatemedia.image_description=image_description
#             updatemedia.video=video
#             updatemedia.video_description=video_description

#             updatemedia.save
#             messages.success(request, 'Information updated successfully')
#             return redirect("admin-home")
        
#         elif request.method=='GET':
#             return render(request, "")                                         #check (html)

#     except Exception as ex:
#         print(ex)
    


# def DeleteMedia(request, id):
#     try:
#         deletemedia = MediaView.objects.get(pk = id).delete()

#         messages.error(request, 'Information Deleted')
#         return redirect("")                                                 #check (url name)

#     except Exception as ex:
#         print(ex)