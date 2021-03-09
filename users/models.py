from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True,blank=False,null=False)
    REQUIRED_FIELDS = ['first_name','last_name','email']

    def __str__(self):
        return self.username
    

