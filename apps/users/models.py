# Third Party Stuff
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.contrib.postgres.fields import CIEmailField
from django.db import models
from django.utils import timezone

# User Stuff
from apps.base.models import BaseModel, UUIDModel

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
        self,
        email: str,
        password: str,
        is_staff: bool,
        is_superuser: bool,
        **extra_fields
    ):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            **extra_fields
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password=None, **extra_fields):
        """Creates and saves a User with the given email and password."""
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class User(AbstractBaseUser, UUIDModel, PermissionsMixin):
    first_name = models.CharField(max_length=120, blank=True)
    last_name = models.CharField(max_length=120, blank=True)

    # A computed field in pre_save. Don't edit this field manually.
    full_name = models.CharField(max_length=240, blank=True)

    # https://docs.djangoproject.com/en/1.11/ref/contrib/postgres/fields/#citext-fields
    email = models.EmailField(unique=True, db_index=True)
    is_staff = models.BooleanField(default=False,
        help_text="Designates whether the user can log into this admin site.",
    )

    can_manage_groups = models.BooleanField(
        default=False,
        help_text="Designates whether the user can manage groups for other user",
    )

    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as "
        "active. Unselect this instead of deleting accounts.",
    )
    date_joined = models.DateTimeField(default=timezone.now)
    verified_on = models.DateTimeField(null=True, db_index=True)

    phone_number = models.CharField(null=True, blank=True)

    USERNAME_FIELD = "email"
    objects = UserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ("-date_joined",)

    def __str__(self):
        return "{} - {}".format(self.id, self.email)

    def is_verified(self):
        return bool(self.verified_on)

    def get_full_name(self) -> str:
        """Returns the first_name plus the last_name, with a space in between."""
        full_name = "{} {}".format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self) -> str:
        """Returns the short name for the user."""
        return self.first_name.strip()