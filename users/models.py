from django.db import models

from django.contrib.auth.models import AbstractUser


class BiblioUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/')
    phone = models.CharField(max_length=15)
