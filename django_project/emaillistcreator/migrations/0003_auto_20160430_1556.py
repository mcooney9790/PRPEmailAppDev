# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emaillistcreator', '0002_auto_20160427_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='docfile',
            field=models.FileField(upload_to='/home/email_attachments/'),
        ),
    ]
