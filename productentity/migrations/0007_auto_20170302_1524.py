# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-02 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productentity', '0006_auto_20170302_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='updated_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='updated_date'),
        ),
    ]
