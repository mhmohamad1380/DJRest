import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    is_verified = models.BooleanField(default=False)
    verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)
