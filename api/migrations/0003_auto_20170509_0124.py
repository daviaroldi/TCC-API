# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-09 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170509_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
