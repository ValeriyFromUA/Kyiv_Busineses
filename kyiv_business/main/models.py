from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"


class Client(models.Model):
    name = models.CharField(max_length=500, null=True, )
    type = models.CharField(max_length=500, null=True)
    activity = models.CharField(max_length=2000, null=True)
    address = models.CharField(max_length=500, null=True)
    phone = models.CharField(max_length=500, null=False)
    email = models.CharField(max_length=500, null=False)
    url = models.CharField(max_length=500, null=False)
    description = models.CharField(max_length=2000, null=False)

    class Meta:
        verbose_name = "Клієнт"
        verbose_name_plural = "Клієнти"
