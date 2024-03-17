from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import *
from emailsend import OTGGenerator
from datetime import datetime, timezone

# Create your views here.


def home(request):
    try:
        birthday = Birthday.objects.filter(is_removed=False)
        testimony = Testimony.objects.filter(is_removed=False).order_by('-date_created')[:4]
        event = Event.objects.first()
        announcement = Announcement.objects.filter(is_removed=False)

        if len(announcement) != 0:
            announcement = Announcement.objects.filter(is_removed=False)[0]

            date_created = event.date_created.strftime('%A')
            current_date = datetime.now(timezone.utc).strftime('%A')

            if date_created != current_date:
                event.service_display = None
                event.save()
            
            return render(request, "index.html", {"event": event, "testimonys": testimony, "birthdays": birthday, "announcement": announcement})

        else:
            date_created = event.date_created.strftime('%A')
            current_date = datetime.now(timezone.utc).strftime('%A')

            if date_created != current_date:
                event.service_display = None
                event.save()
            
            return render(request, "index.html", {"event": event, "testimonys": testimony, "birthdays": birthday})
    
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



def picture(request):
    try:
        return render(request, "picture.html")
    
    except Exception as ex:
        print(ex)



def testimonies(request):
    try:
        testimony = Testimony.objects.filter(is_removed=False).order_by('-date_created')
        return render(request, "testimonies.html", {"testimonys": testimony})

    except Exception as ex:
        print(ex)



def services(request):
    try:
        testimony = Testimony.objects.filter(is_removed=False).order_by('-date_created')[:4]
        return render(request, "services.html", {"testimonys": testimony})
    
    except Exception as ex:
        print(ex)



def fourCorners(request):
    try:
        return render(request, "four-corners.html")
    
    except Exception as ex:
        print(ex)



def twelvePillars(request):
    try:
        pillar = Team.objects.filter(is_removed=False).order_by('date_created')
        return render(request, "twelve-pillars.html", {"pillars": pillar})
    
    except Exception as ex:
        print(ex)



def sermonExcerpt(request):
    try:
        excerpt = Sermon.objects.filter(is_removed=False).order_by('-date_created')[:12]
        return render(request, "sermon.html", {"excerpts": excerpt})

    except Exception as ex:
        print(ex)



def sermonExcerptById(request, id):
    try:
        excerpt = Sermon.objects.get(pk = id)
        related_excerpt = Sermon.objects.filter(is_removed=False).order_by('-date_created')[:3]
        
        return render(request, "sermon_excerpt.html", {"excerpt": excerpt, "related_excerpts": related_excerpt})

    except Exception as ex:
        print(ex)



def prayerRequest(request):
    try:
        if request.method=="POST":
            name = request.POST['name']
            # country = request.POST['country']
            email = request.POST['email']
            # phone_number = request.POST['phone_no']
            message = request.POST['message']

            prayer_request = PrayerRequest(
                name=name,
                # country=country,
                email=email,
                # phone_number=phone_number,
                message=message
                )
            prayer_request.save()

            OTGGenerator([email], "SUCCESSFUL SUBMISSION OF PRAYER REQUEST!!!", """We kindly inform you that your prayer request has been sent to the church for prior attention. Keep your faith steadfast in the Lord Jesus. God bless you.""")
            return redirect("home")

    except Exception as ex:
        print(ex)



def devotionalLetter(request):
    try:
        if request.method=="POST":
            email = request.POST['devotional_email']

            devotional_letter = DevotionalLetter(
                email=email
                )
            devotional_letter.save()

            OTGGenerator([email], "SUBSCRIBTION TO DEVOTIONAL LETTER!!!", """We kindly inform you that you have subscribe to our devotional letter for frequent biblical and spiritual devotions.""")
            return redirect("home")

    except Exception as ex:
        print(ex)



def contactInquiry(request):
    try:
        if request.method=="POST":
            name = request.POST['name']
            email = request.POST['email']
            inquiry = request.POST['inquiry']

            contact_inquiry = Inquiry(
                name=name,
                email=email,
                inquiry=inquiry
                )
            contact_inquiry.save()

            OTGGenerator([email], "SUCCESSFUL SUBMISSION OF INQUIRY!!!", """We kindly inform you that your inquiry has been sent to the church for prior attention. We will get back to you shortly. Thank you.""")
            return redirect("contact")

    except Exception as ex:
        print(ex)
