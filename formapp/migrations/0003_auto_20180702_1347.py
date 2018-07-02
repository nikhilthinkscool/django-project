# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-02 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0002_auto_20180702_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='phoneno',
            new_name='number',
        ),
        migrations.AddField(
            model_name='signup',
            name='education',
            field=models.CharField(choices=[('UR', 'undergraduated'), ('GR', 'graduated'), ('PG', 'postgraduated')], default='UR', max_length=2),
        ),
        migrations.AddField(
            model_name='signup',
            name='gender',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], default='m', max_length=1),
        ),
    ]
