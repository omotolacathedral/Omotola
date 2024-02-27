from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    event_announcement = models.TextField(null=True, blank=True)
    periodic_display = models.TextField(null=True, blank=True)
    service_display = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)



class Testimony(models.Model):
    testifier_name = models.CharField(max_length=250)
    testimony_content = models.CharField(max_length=250)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.testifier_name}"



class Office(models.Model):
    title = models.CharField(max_length=250)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Team(models.Model):
    office = models.OneToOneField(Office, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.office.title} - {self.name}"



class DevotionalLetter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return f"{self.email}"



class PrayerRequest(models.Model):
    name  = models.CharField(max_length=250, null=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.email}"
    









# class GeneralView(models.Model):
#     favicon = models.TextField()
#     church_logo = models.TextField()

 

# class HomeView(models.Model):
#     front_video = models.FileField(upload_to="video", null=True, blank=True)
#     front_image = models.TextField(null=True, blank=True)
#     evangelism_topic = models.CharField(max_length=50, null=True, blank=True)
#     evangelism_content = models.CharField(max_length=250, null=True, blank=True)
#     evangelism_image = models.TextField(null=True, blank=True)
#     timestamp = models.DateTimeField(auto_now_add=True) 



# class BlogView(models.Model):
#     topic = models.CharField(max_length=250)
#     content = models.TextField()
#     image = models.TextField(null=True, blank=True)
#     timestamp = models.DateTimeField(auto_now_add=True)



# class MediaView(models.Model):
#     image = models.TextField()
#     image_description = models.TextField(null=True, blank=True)
#     video = models.FileField(upload_to="video", null=True, blank=True)
#     video_description = models.TextField(null=True, blank=True)
#     timestamp = models.DateTimeField(auto_now_add=True) 