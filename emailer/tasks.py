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


@shared_task
def send_daily_summary_email():
    print("Sending daily summary email")
    send_mail(
        subject="Daily summary",
        message="Here is your daily summary",
        from_email=None,
        recipient_list=["tazulislam42609770@gmail.com"]
    )
    return "Daily summary sent"