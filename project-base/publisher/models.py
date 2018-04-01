from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=254, blank=False, unique=True)
    username = models.CharField(max_length=100, blank=False)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    password1 = models.CharField(max_length=12, blank=False)
    password2 = models.CharField(max_length=12, blank=False)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username