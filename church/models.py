from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Announcement(models.Model):
    event_announcement = models.TextField(default=None, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_removed = models.BooleanField(default=False, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)



class Event(models.Model):
    periodic_display = models.TextField(null=True, blank=True)
    service_display = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_removed = models.BooleanField(default=False, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)



class Birthday(models.Model):
    image = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_removed = models.BooleanField(default=False, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)



class Testimony(models.Model):
    testifier_name = models.CharField(max_length=250)
    testimony_content = models.CharField(max_length=250)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_removed = models.BooleanField(default=False, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.testifier_name}"



class Office(models.Model):
    title = models.CharField(max_length=250)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_removed = models.BooleanField(default=False, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"



class Team(models.Model):
    office = models.OneToOneField(Office, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    image = models.TextField(default=None, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_removed = models.BooleanField(default=False, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.office.title} - {self.name}"
    


class Sermon(models.Model):
    service_type = models.CharField(max_length=250, null=True, blank=True)
    sermoner_picture = models.TextField()
    sermoner = models.CharField(max_length=250)
    topic = models.CharField(max_length=250)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_removed = models.BooleanField(default=False, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_type} - {self.sermoner}"
   


class DevotionalLetter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return f"{self.email}"



class PrayerRequest(models.Model):
    name  = models.CharField(max_length=250, null=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.email}"
    


class Inquiry(models.Model):
    name  = models.CharField(max_length=250, null=True)
    email = models.EmailField()
    inquiry = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.email}"
    