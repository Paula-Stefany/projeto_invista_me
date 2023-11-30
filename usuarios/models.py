from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username_validator = UnicodeUsernameValidator

    email = models.EmailField(
        _('email address'),
        unique=True)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=False,
        blank=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



