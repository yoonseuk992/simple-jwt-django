from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'email'

    objects = BaseUserManager()
