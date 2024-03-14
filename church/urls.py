from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="services"),
    path("testimonies/", views.testimonies, name="testimonies"),
    path("four-corners/", views.fourCorners, name="four-corners"),
    path("twelve-pillars/", views.twelvePillars, name="twelve-pillars"),

    path("prayer-request", views.prayerRequest, name="prayer-request"),
    path("devotional-letter", views.devotionalLetter, name="devotional-letter"),
    path("contact-inquiry", views.contactInquiry, name="contact-inquiry"),
]