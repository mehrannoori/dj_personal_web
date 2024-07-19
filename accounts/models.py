from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Meta:
        permissions = [
            ('account_permissions', 'can edit users account'),
        ]
    pass