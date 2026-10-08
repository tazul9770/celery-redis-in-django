from django.core.mail import send_mail
from celery import shared_task

@shared_task
def send_to_email(to_email):
    print(to_email)
    send_mail(
        subject="Welcome my users",
        message="Thanks for you join our team",
        from_email=None,
        recipient_list=[to_email]
     )
    return f"sent to {to_email}"
