# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-12 15:11
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_image'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('Ktm', django.db.models.manager.Manager()),
            ],
        ),
    ]
