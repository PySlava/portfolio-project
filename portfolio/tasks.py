from django.contrib.auth.models import User
import logging
from myproject.celery import app
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)

@app.task
def send_welcome_email_task(user_id):
    user = User.objects.get(pk=user_id)
    subject = "Hello in our services"
    message = f"Hello, {user}! Thanks for create account in our services"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)


@app.task
def test_task():
    logger.info('Hello, user')
    return 'OK'

