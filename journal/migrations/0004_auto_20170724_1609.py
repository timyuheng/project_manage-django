# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_auto_20170705_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userjournal',
            name='date',
            field=models.DateField(verbose_name='日期'),
        ),
    ]
