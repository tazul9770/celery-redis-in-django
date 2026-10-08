from django.shortcuts import render
from emailer.tasks import send_to_email

def home(request):
    return render(request, "home.html")

def send_welcome_email(request):
    recipients = [f"user{i}@example.com" for i in range(1, 40)]
    for email in recipients:
        send_to_email.delay(email)
    return render(request, "success.html", {"count":len(recipients)})
