# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 09:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentLogin', '0006_auto_20170921_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_details',
            name='email_id',
        ),
    ]