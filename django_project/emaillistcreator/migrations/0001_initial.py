# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='https://emailappstatic.s3.amazonaws.com/media/contactlists/')),
            ],
        ),
    ]
