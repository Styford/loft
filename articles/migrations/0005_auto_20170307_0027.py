# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 17:27
from __future__ import unicode_literals

from django.db import migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_comments_comments_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_extraText',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
    ]
