from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_welcome_email_task

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_welcome_email_task.delay(instance.id)