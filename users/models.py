from django.db import models
from django.contrib.auth.models import AbstractUser
import logging

# Get an instance of a logger
logger = logging.getLogger('django')

class BiblioUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, default='')

    class Meta:
        permissions = (
            ('can_rent', 'użytkownik może wypożyczać książki'),
        )