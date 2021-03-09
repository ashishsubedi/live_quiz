from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from rest_framework.authtoken.models import Token

from .models import Profile
from django.conf import settings
User = settings.AUTH_USER_MODEL

@receiver(post_save,sender=User)
def post_save_user_create(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        Token.objects.create(user=instance)

@receiver(post_delete,sender=User)
def post_delete_user_delete(sender,instance,**kwargs):
    profile = Profile.objects.filter(user=instance)
    if profile.exists():
        profile.first().delete()

