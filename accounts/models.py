from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class UserInfo(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)