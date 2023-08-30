"""
Database models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        if not email:
            raise ValueError("User must have an email address.")

        print(f"called create_user with: {email}, {password}")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create, save and return a new superuser"""

        if not email:
            raise ValueError("Superuser must have an email address.")


        print(f"Called create_superuser with: {email}, {password}")
        super_user = self.model(email=self.normalize_email(email=email), **extra_fields)
        super_user.is_staff = True
        super_user.is_superuser = True
        super_user.set_password(password)
        super_user.save(using=self._db)

        return super_user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'