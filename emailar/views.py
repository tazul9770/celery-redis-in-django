from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', )

def send_welcome_email(request):
    recipients = [f"user{i}@example.com" for i in range(1, 15)]

    for email in recipients:
        send_mail(
            subject="Welcome...",
            message="Thanks for your kindness",
            from_email=None,
            recipient_list=[email]
        )
    return render(request, "success.html", {"count":len(recipients)})
