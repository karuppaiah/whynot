# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-02 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productentity', '0005_auto_20170302_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdata',
            name='created_date',
            field=models.DateTimeField(verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='created_date',
            field=models.DateTimeField(verbose_name='created_date'),
        ),
    ]
