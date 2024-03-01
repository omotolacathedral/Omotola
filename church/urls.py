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

    # path("home/create", views.CreateGeneral),
    # path("home/getall/", views.GetAllGeneral),
    # path("home/getid/<str:id>/", views.GetGeneralById),
    # path("home/update/<str:id>/", views.UpdateGeneral),
    # path("home/delete/<str:id>/", views.DeleteGeneral),

    # path("home/create", views.CreateHome),
    # path("home/getall/", views.GetAllHome),
    # path("home/getid/<str:id>/", views.GetHomeById),
    # path("home/update/<str:id>/", views.UpdateHome),
    # path("home/delete/<str:id>/", views.DeleteHome),

    # path("blog/create", views.CreateBlog),
    # path("blog/getall/", views.GetAllBlog),
    # path("blog/getid/<str:id>/", views.GetBlogById),
    # path("blog/update/<str:id>/", views.UpdateBlog),
    # path("blog/delete/<str:id>/", views.DeleteBlog),

    # path("media/create", views.CreateMedia),
    # path("media/getall/", views.GetAllMedia),
    # path("media/getid/<str:id>/", views.GetMediaById),
    # path("media/update/<str:id>/", views.UpdateMedia),
    # path("media/delete/<str:id>/", views.DeleteMedia),
]