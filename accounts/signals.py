from accounts.models import Profile 
from django.contrib.auth import get_user_model
from django.conf import settings 
from django.db.models.signals import post_save
from django.dispatch import receiver 

# User=settings.AUTH_USER_MODEL
User=get_user_model()
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(person=instance)      