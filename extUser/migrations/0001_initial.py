# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 09:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='extUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_key', models.CharField(max_length=30)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='img/avatars/', verbose_name='\u0410\u0432\u0430\u0442\u0430\u0440\u043a\u0430')),
                ('user_key', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'extUser',
            },
        ),
    ]
