# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171112_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='classifier',
            name='path_to_bin',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
