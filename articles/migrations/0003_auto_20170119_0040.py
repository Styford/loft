# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_likes',
            field=models.IntegerField(blank=True),
        ),
    ]