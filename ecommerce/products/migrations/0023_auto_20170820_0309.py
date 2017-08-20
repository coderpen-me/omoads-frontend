# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20170819_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='zones',
            field=models.ManyToManyField(to='products.Zone', null=True, blank=True),
        ),
    ]
