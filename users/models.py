from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(blank=False,unique=True)
    REQUIRED_FIELDS = ['first_name','email','last_name']


class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)

    bio = models.TextField(blank=True, default="My Bio..")
    avatar = models.ImageField(upload_to='avatar',default='avatar.png',blank=True)

    def __str__(self):
        return f"{self.user.username} profile"
