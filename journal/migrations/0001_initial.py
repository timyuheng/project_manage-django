# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 08:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserJournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='日期')),
                ('work_today', models.CharField(max_length=200, verbose_name='今日工作')),
                ('question', models.CharField(blank=True, max_length=200, verbose_name='问题&风险')),
                ('plan_tomorrow', models.TextField(verbose_name='明日计划')),
                ('usr_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
