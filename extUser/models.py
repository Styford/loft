# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class extUser(models.Model):
    class Meta:
        db_table = "extUser"                # Название таблицы в БД

    user_key = models.OneToOneField(User)
    secret_key = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to="media/img/avatars/", null=True, blank=True, default="media/img/avatars/crip.png")
    department = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):                  # Название объекта в админке
        return self.user_key.username


# Create your models here.