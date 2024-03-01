from django.urls import path
from . import views


urlpatterns = [
    path("admin/testimony/", views.adminTestimony, name="admin-testimony"),
    path("admin/testimony/add/", views.newTestimony, name="new-testimony"),
    path("admin/twelve-pillar/", views.adminTwelvePillar, name="admin-twelve-pillar"),
    path("admin/twelve-pillar/add/", views.newTwelvePillar, name="new-twelve-pillar"),
    path("admin/birthday/", views.adminBirthday, name="admin-birthday"),
    path("admin/birthday/add/", views.newBirthday, name="new-birthday"),
    path("admin/event/", views.adminEvent, name="admin-event"),
    path("admin/event/add/", views.newEvent, name="new-event"),

    path("admin/register", views.registerStaff, name="register"),
    path("", views.loginStaff, name="login"),
    path("admin/logout", views.logoutStaff, name="logout"),

    path("admin/getall/", views.getAllStaff, name="get-all-staffs"),
    path("admin/getid/<str:id>/", views.getById, name="get-byid-staff"),
    # path("admin/update/<str:id>/", views.updateStaff name="update-staff"),
    path("admin/delete/<str:id>/", views.deleteStaff, name="delete-staff"),
]