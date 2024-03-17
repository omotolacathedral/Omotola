from django.urls import path
from . import views


urlpatterns = [
    path("admin/announcement/", views.adminAnnouncement, name="admin-announcement"),
    path("admin/announcement/add/", views.newAnnouncement, name="new-announcement"),
    path("admin/announcement/update/<str:id>/", views.updateAnnouncement, name="update-announcement"),
    path("admin/announcement/delete/<str:id>/", views.deleteAnnouncement, name="delete-announcement"),

    path("admin/event/", views.adminEvent, name="admin-event"),
    path("admin/event/add/", views.newEvent, name="new-event"),
    path("admin/event/update/<str:id>/", views.updateEvent, name="update-event"),
    path("admin/event/delete/<str:id>/", views.deleteEvent, name="delete-event"),

    path("admin/birthday/", views.adminBirthday, name="admin-birthday"),
    path("admin/birthday/add/", views.newBirthday, name="new-birthday"),
    path("admin/birthday/update/<str:id>/", views.updateBirthday, name="update-birthday"),
    path("admin/birthday/delete/<str:id>/", views.deleteBirthday, name="delete-birthday"),

    path("admin/testimony/", views.adminTestimony, name="admin-testimony"),
    path("admin/testimony/add/", views.newTestimony, name="new-testimony"),
    path("admin/testimony/update/<str:id>/", views.updateTestimony, name="update-testimony"),
    path("admin/testimony/delete/<str:id>/", views.deleteTestimony, name="delete-testimony"),

    path("admin/office/", views.adminOffice, name="admin-office"),
    path("admin/office/add/", views.newOffice, name="new-office"),
    path("admin/office/update/<str:id>/", views.updateOffice, name="update-office"),
    path("admin/office/delete/<str:id>/", views.deleteOffice, name="delete-office"),

    path("admin/twelve-pillar/", views.adminTwelvePillar, name="admin-twelve-pillar"),
    path("admin/twelve-pillar/add/", views.newTwelvePillar, name="new-twelve-pillar"),
    path("admin/twelve-pillar/update/<str:id>/", views.updateTwelvePillar, name="update-twelve-pillar"),
    path("admin/twelve-pillar/delete/<str:id>/", views.deleteTwelvePillar, name="delete-twelve-pillar"),

    path("admin/sermon-excerpt/", views.adminSermonExcerpt, name="admin-sermon-excerpt"),
    path("admin/sermon-excerpt/add/", views.newSermonExcerpt, name="new-sermon-excerpt"),
    path("admin/sermon-excerpt/update/<str:id>/", views.updateSermonExcerpt, name="update-sermon-excerpt"),
    path("admin/sermon-excerpt/delete/<str:id>/", views.deleteSermonExcerpt, name="delete-sermon-excerpt"),

    path("admin/register", views.registerStaff, name="register"),
    path("", views.loginStaff, name="login"),
    path("admin/logout", views.logoutStaff, name="logout"),

    path("admin/profiles/", views.getAllStaffs, name="get-all-staffs"),
    path("admin/delete/<str:id>/", views.deleteStaff, name="delete-staff"),
]