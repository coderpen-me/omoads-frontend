# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_priceperiod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_facing',
            field=models.CharField(default=b'Facing IMS', max_length=200),
        ),
    ]
