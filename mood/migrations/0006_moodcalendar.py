# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-25 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood', '0005_verblist'),
    ]

    operations = [
        migrations.CreateModel(
            name='moodCalendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=20)),
                ('moodDate', models.DateTimeField(auto_now_add=True)),
                ('verblist', models.CharField(max_length=1000)),
                ('color', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('startNum', models.FloatField(default=0, null=True)),
                ('endNum', models.FloatField(default=0, null=True)),
            ],
        ),
    ]
