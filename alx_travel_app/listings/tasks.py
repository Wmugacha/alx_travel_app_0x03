from celery import Celery
from django.core.mail import send_mail
from django.conf import settings
import logging
from alx_travel_app.celery import app

logger = logging.getLogger(__name__)

@app.task(bind=True, max_retries=3)
def send_payment_confirmation_email(self, user_email, listing_title):
    try:
        logger.info(f"Sending confirmation email to {user_email} for {listing_title}")
        subject = "Your Payment is Confirmed"
        message = f"Hi, your booking for {listing_title} has been confirmed. \nThank you for choosing to stay with us."
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user_email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    except Exception as exc:
        logger.error(f"Error sending email: {exc}")

        self.retry(countdown=60, exc=exc)


@app.task(bind=True, max_retries=3)
def send_booking_confirmation_email(self, user_email, listing_title):
    try:
        logger.info(f"Sending confirmation email to {user_email} for {listing_title}")
        subject = "Your Booking is Confirmed"
        message = f"Hi, your booking for {listing_title} has been confirmed. \nThank you for your payment."
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user_email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    except Exception as exc:
        logger.error(f"Error sending email: {exc}")

        self.retry(countdown=60, exc=exc)