from django.urls import path
from emailer.views import home, send_welcome_email

urlpatterns = [
    path('', home, name="home"),
    path('send_welcome_email', send_welcome_email, name="send-welcome-email")
]
