# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-10 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reversion', '0003_fill_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='reverted_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='reverted at'),
        ),
    ]
