from django.urls import path

from common.core import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path('send-email/', views.send_test_email), # TODO remove in production
]
