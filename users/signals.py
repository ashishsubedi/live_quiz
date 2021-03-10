from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model
User = get_user_model()

@receiver(post_save,sender=User)
def post_save_user_create(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)
