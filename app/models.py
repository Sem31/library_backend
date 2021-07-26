from typing import Tuple
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=30,null=True, blank=True)
    email = models.EmailField(_('email address'),unique=True)
    phone = models.CharField(max_length=10)
    address  = models.TextField()
    profile = models.ImageField(null=True, blank=True)
    is_member = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
    	return self.email