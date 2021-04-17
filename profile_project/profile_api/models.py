from django.db import models
from .manager import CustomUserManager
# from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin





class CustomUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=100, unique=True)
    username=models.CharField(max_length=200)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username',]

    objects=CustomUserManager()

    def __str__(self):
        return self.username

    def full_name(self):
        return f'{self.first_name} {self.last_name}'



