# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-29 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood', '0007_auto_20161027_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='resultText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
            ],
        ),
    ]
