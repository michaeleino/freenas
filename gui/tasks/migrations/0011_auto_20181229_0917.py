# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-29 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import freenasUI.freeadmin.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_auto_20181210_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloudsync',
            name='follow_symlinks',
            field=models.BooleanField(default=False, help_text='Follow symlinks and copy the pointed to item.', verbose_name='Follow symlinks'),
            preserve_default=False,
        ),
    ]
