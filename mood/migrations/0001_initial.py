# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-29 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=40, null=True)),
                ('emotion', models.CharField(blank=True, max_length=100, null=True)),
                ('mood_Verb', models.CharField(blank=True, max_length=100, null=True)),
                ('mood_Amount', models.FloatField(default=0, null=True)),
            ],
        ),
    ]
