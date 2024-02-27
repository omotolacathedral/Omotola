from django.urls import path
from . import views


urlpatterns = [
    path("admin/register", views.RegisterStaff, name="register"),
    path("admin/login", views.LoginStaff, name="login"),
    path("admin/logout", views.LogoutStaff, name="logout"),

    path("admin/getall/", views.GetAllStaff, name="get-all-staffs"),
    path("admin/getid/<str:id>/", views.GetById, name="get-byid-staff"),
    # path("admin/update/<str:id>/", views.UpdateStaff name="update-staff"),
    path("admin/delete/<str:id>/", views.DeleteStaff, name="delete-staff"),
]