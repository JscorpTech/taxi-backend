from django.contrib.auth import models as auth_models
from django.db import models

from ..choices import RoleChoice
from ..managers import UserManager
from functools import cached_property


class User(auth_models.AbstractUser):
    phone = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    validated_at = models.DateTimeField(null=True, blank=True)
    role = models.CharField(
        max_length=255,
        choices=RoleChoice,
        default=RoleChoice.USER,
    )

    USERNAME_FIELD = "phone"
    objects = UserManager()

    @cached_property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            phone="998888112309",
        )

    def __str__(self):
        return self.phone
