# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 16:20
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emaillistcreator', '0004_auto_20160430_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='docfile',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/email_attachments'), upload_to=b''),
        ),
        migrations.AlterField(
            model_name='contactfile',
            name='docfile',
            field=models.FileField(upload_to='contactlists'),
        ),
    ]
