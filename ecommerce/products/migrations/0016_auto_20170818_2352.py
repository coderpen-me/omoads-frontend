# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20170815_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_facing',
            field=models.CharField(max_length=200, default='Facing IMS'),
        ),
    ]
