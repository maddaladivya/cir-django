# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentLogin', '0007_remove_student_details_email_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='no_of_current_Arrears',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='no_of_history_Arrears',
            field=models.IntegerField(default=0),
        ),
    ]