# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('si', models.URLField(max_length=128, unique=True)),
                ('ip', models.CharField(max_length=128)),
                ('org', models.CharField(max_length=128)),
            ],
        ),
    ]