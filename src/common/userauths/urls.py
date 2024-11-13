from django.urls import path

from common.userauths import views

app_name = "userauths"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("check/", views.check_username_availability, name="check"),
]
