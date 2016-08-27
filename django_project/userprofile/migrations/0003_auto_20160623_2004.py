# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-23 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_remove_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='profile',
            name='google_username',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
