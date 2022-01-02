from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin,
    AbstractBaseUser
)
from .objects import BaseUserManager
from site_back.common.models import BaseModel


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name="username",
        max_length=50,
        unique=True,
        blank=False,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        blank=False,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = BaseUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin
