# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cir', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_details',
            name='document',
            field=models.FileField(default='null', upload_to='documents/'),
        ),
    ]
