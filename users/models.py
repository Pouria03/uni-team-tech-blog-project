from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import UserManager

from django.contrib.auth.models import Permission


class User(AbstractBaseUser, PermissionsMixin):
    """ 
    This is User model that email is the unique identifiers
    for authentication instead of usernames.
    """
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.email + '-' + self.full_name

    def save(self, *args, **kwargs):
        """ if user is staff, then add some permissions to the user """
        if self.is_staff == True:
            permit = Permission.objects.get(codename='view_contenttype')
            self.user_permissions.add(permit)
            self.full_name += '- STAFF'

        super().save(*args, **kwargs)