# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cir', '0002_auto_20170802_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_details',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
