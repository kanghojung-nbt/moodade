# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-04 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_keyboard'),
    ]

    operations = [
        migrations.DeleteModel(
            name='KaKAoMood',
        ),
        migrations.DeleteModel(
            name='Keyboard',
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
