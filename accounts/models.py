from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('farmer', 'Farmer'),
        ('customer', 'Customer'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username