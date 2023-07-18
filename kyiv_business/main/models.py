from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"


class Activity(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'activity'
        verbose_name = "Сфера діяльності"
        verbose_name_plural = "Сфери діяльності"


class Company(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    url = models.URLField(max_length=255)
    description = models.TextField()

    activities = models.ManyToManyField(Activity, through='CompanyActivityAssociation', related_name='companies')

    class Meta:
        managed = False
        db_table = 'company'
        verbose_name = "Компанія"
        verbose_name_plural = "Компанії"


class CompanyActivityAssociation(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    activity = models.ForeignKey('Activity', on_delete=models.CASCADE)

    class Meta:
        db_table = 'company_activity_association'
        managed = False
